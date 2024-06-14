{
  description = "Shreddit cleans your reddit history";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
    ...
  }: let
    allSystems = [
      "aarch64-darwin"
      "aarch64-linux"
      "x86_64-darwin"
      "x86_64-linux"
    ];
    # Helper to provide system-specific attributes
    forAllSystems = f:
      nixpkgs.lib.genAttrs allSystems
      (system: f {pkgs = import nixpkgs {inherit system;};});
  in {
    devShells = forAllSystems ({pkgs}: {
      default = let
        python = pkgs.python311;
      in
        pkgs.mkShell {
          packages = [
            # Python plus helper tools
            (python.withPackages (ps:
              with ps; [
                # Formatting
                black
                # setuptools
              ]))
          ];
        };
    });
    packages = forAllSystems ({pkgs}: {
      default = let
        python = pkgs.python311;
        pythonPackages = pkgs.python311Packages;
        pythonWithPkgs = python.withPackages (pythonPkgs:
          with pythonPkgs; [
            # This list contains tools for Python development.
            # You can also add other tools, like black.
            #
            # Note that even if you add Python packages here like PyTorch or Tensorflow,
            # they will be reinstalled when running `pip -r requirements.txt` because
            # virtualenv is used below in the shellHook.
            # ipython
            pip
            setuptools
            # virtualenvwrapper
            wheel
            black
          ]);

        backports-abc = let
          pname = "backports_abc";
          version = "0.5";
        in
          pythonPackages.buildPythonPackage {
            inherit pname version;
            src = pkgs.fetchPypi {
              inherit pname version;
              sha256 = "sha256-AzvlRRSgPiVd91xa7o+eZy9mP5OrtyNETK7I/kNDe94=";
            };
            doCheck = false;
          };
      in
        with pythonPackages;
        # python.withPackages (ps:
          buildPythonApplication rec {
            pname = "shreddit";
            version = "0.6.0";
            src = ./.;
            pyproject = true;
            # build-system = buildSystem;
            # build-system = [
            #   setuptools
            # ];
            propagatedBuildInputs = [
              setuptools

              pyyaml
              appdirs
              arrow
              backports-abc
              praw
              requests
              tornado
              prometheus-client
            ];
            nativeBuildInputs = [
              setuptools
              wheel
            ];
          };
      # );
    });
    # };
    formatter = forAllSystems ({pkgs}: pkgs.alejandra);
  };
}
