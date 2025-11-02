# Shreddit

> **About the Original Repository**: The original x89/Shreddit repository was renamed to "Solana-Arbitrage-Bot" and [all Shreddit code was replaced with unrelated cryptocurrency code](https://github.com/x89/Solana-Arbitrage-Bot/pull/185) around mid-2024. All original issues, stars, and history were transferred to that renamed repository, which is why this repo appears to be a "fork" of a Solana bot instead of the original Shreddit. This fork maintains the original Shreddit functionality with security updates and is considered feature-complete. For an alternative implementation, see the [Rust rewrite](https://github.com/andrewbanchich/shreddit) (note: feature parity may differ).

This also includes changes from the [pythonInRelay/Shreddit](https://github.com/pythonInRelay/Shreddit) fork.

## Docker
This is the recommended route. If you run into a bug, please ensure it is reproducible inside of docker. I will not troubleshoot local installations.

Create a `config` directory. This should include your `praw.ini` and `shreddit.yml` config files. We will mount this into the docker container.

```bash
docker run --rm -v $(pwd)/config:/config ghcr.io/kusold/shreddit:latest
```

I will not be adding cron support inside of the container. You can run the container on a cron schedule if you desire.

`latest` is updated everytime a tag is created. `master` is updated on every merge to master.

### Using Apple Container (macOS)

If you're on a Mac with Apple silicon, you can use [Apple's Container framework](https://github.com/apple/container) for a faster, native container experience optimized for macOS.

#### Prerequisites

Install Apple Container (requires macOS 15 or later, macOS 26 recommended):

```bash
# Download the latest installer from https://github.com/apple/container/releases
# Double-click the .pkg file and follow the installation instructions

# Start the container service
container system start
```

#### Building the image

Build the Shreddit image locally:

```bash
# Clone the repository
git clone https://github.com/kusold/Shreddit.git
cd Shreddit

# Build the image
container build --tag shreddit:latest --file Dockerfile .
```

#### Running with Apple Container

Run Shreddit using Apple Container:

```bash
# Create your config directory with praw.ini and shreddit.yml
mkdir -p config

# Run the container
container run --rm -v $(pwd)/config:/config shreddit:latest
```

Or run it in detached mode:

```bash
container run --name shreddit --detach --rm -v $(pwd)/config:/config shreddit:latest

# View logs
container logs shreddit

# Stop the container
container stop shreddit
```

#### Pulling from a registry

You can also pull and run the pre-built image from GitHub Container Registry:

```bash
# Pull the image
container image pull ghcr.io/kusold/shreddit:latest

# Run it
container run --rm -v $(pwd)/config:/config ghcr.io/kusold/shreddit:latest
```

## Installation with uv

This project uses [uv](https://github.com/astral-sh/uv) for fast, reliable package management.

**Requirements**: Python 3.12 or higher

### Prerequisites

Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation

1. Clone the `shreddit` repository:
   ```bash
   git clone https://github.com/kusold/Shreddit.git
   cd Shreddit
   ```

2. Install the package using uv:
   ```bash
   uv pip install .
   ```

   Or to install in a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install .
   ```

## Post-install steps

After installing the `shreddit` command line utility, the first step is setting up the tool's configuration files.
Simply typing `shreddit -g` will generate configs. After configuring your user credentials and deletion scope (in the created praw.ini), running the tool with the `shreddit`
command will begin the tool's operation. Sit back and wait for it to parse each comment.

### Configuring Credentials

Running `shreddit -g` will generate a blank praw.ini file that looks like this:

```
# Credentials go here. Fill out default, or provide one or more names and call shreddit with the -u option to specify
# which set to use.
[default]
client_id=
client_secret=
username=
password=
ratelimit_seconds=31 ## HIGHLY RECOMMENDED as Reddit now limits API calls
```

**You must provide values for each of these.** As strange as it may seem to provide both a username/password pair *and*
a client id/secret pair, that is how the Reddit API does "OAuth" script applications.

Username and password are simply your Reddit login credentials for the account that will be used. However, to obtain the
client ID and secret, follow these steps (taken from 
[PRAW documentation](http://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application)):

1. Open your Reddit application preferences by clicking [here](https://www.reddit.com/prefs/apps/).
2. Add a new application. It doesn't matter what it's named, but calling it "shreddit" makes it easier to remember.
3. Select "script".
4. Redirect URL does not matter for script applications, so enter something like http://127.0.0.1:8080
5. Once created, you should see the name of your application followed by 14 character string. Enter this 14 character
   string as your `client_id`.
6. Copy the 27 character "secret" string into the `client_secret` field.

Finally, your praw.ini should look like this (with fake data provided here):

```
[default]
client_id=f3FaKeD4t40PsJ
client_secret=dfK3pfMoReFAkEDaTa123456789
username=testuser
password=123passwordgoeshere123
```

Keep your praw.ini either in the current directory when running `shreddit`, or in one of the config folders
[described here](http://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html) such as
`~/.config`.

To use more than one account, you can add multiple profiles instead of just `[default]` and use the `-u` option to 
`shreddit` to choose which one each time.

### Automating

The easiest way to automate this tool after the first run is by using the cron utility. Run `crontab -e` to edit your
user's crontab settings.

**Examples:**

The following examples require that the PRAW configuration file is located in the config directory. See [this PRAW
documentation](http://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html) for more information.

- Run every hour on the hour
        `0 * * * * shreddit -c <full path to shreddit.yml>`

- Run at 3am every morning
        `0 3 * * * shreddit -c <full path to shreddit.yml>`

- Run once a month on the 1st of the month
        `0 0 1 * * shreddit -c <full path to shreddit.yml>`

If virtualenv was used, be sure to add `source /full/path/to/venv/bin/activate &&` before the command. For example:

`0 * * * * source /full/path/to/venv/bin/activate && shreddit -c <full path to shreddit.yml>`

### Command Line Options

```
$ shreddit --help
usage: app.py [-h] [-c CONFIG] [-g] [-u USER]

Command-line frontend to the shreddit library.

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Config file to use instead of the default shreddit.yml
  -g, --generate-configs
                        Write shreddit and praw config files to current
                        directory.
  -u USER, --user USER  User section from praw.ini if not default
```
