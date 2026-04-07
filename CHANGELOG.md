# Changelog

All notable changes to this project will be documented in this file.

## [6.5.0](https://github.com/kusold/Shreddit/compare/v6.4.1...v6.5.0) (2026-04-07)

### Features

* **ci:** switch to RenovateBot ([#194](https://github.com/kusold/Shreddit/issues/194)) ([4cd71a4](https://github.com/kusold/Shreddit/commit/4cd71a4fc6997a026a72c564fbd96635b6dd982d))

### Bug Fixes

* add issues write permission to Docker Security Scan workflow ([fe21b44](https://github.com/kusold/Shreddit/commit/fe21b449d49c93b79ac741dc10319d42af0a1eb3))
* **ci:** Fix docker scan reference issues ([d737cd4](https://github.com/kusold/Shreddit/commit/d737cd4ea24fb0faa7bf696a3f8cff5b9d6e213c))
* **ci:** Fix yaml indentation ([d3a47fd](https://github.com/kusold/Shreddit/commit/d3a47fd1765770662ad9a6ce82b695c485c2d59e))
* **ci:** handle missing Docker images in security scan workflow ([#191](https://github.com/kusold/Shreddit/issues/191)) ([c97ab2e](https://github.com/kusold/Shreddit/commit/c97ab2eeb53669016cca79139518bc801707a134))
* replace pkg_resources with importlib.resources for Python 3.14 compat ([f9f6f22](https://github.com/kusold/Shreddit/commit/f9f6f220e0c8a13c38938d03d140d51e9484f3d7))

### Tests

* add smoke test for app entrypoint imports ([c55316c](https://github.com/kusold/Shreddit/commit/c55316cc325a89f5933a139538bc692c2c74e0bb))

### Continuous Integration

* change release workflow to manual trigger ([069149e](https://github.com/kusold/Shreddit/commit/069149ef866e122de025c49dfc6736bde8c9a514))

### Chores

* **ci:** add package rules for dependency update types ([8696a3e](https://github.com/kusold/Shreddit/commit/8696a3ecc6bba3d53adac5534f9caad6352cfa14))
* **ci:** change label to addLabels for GitHub Actions ([9b6e57f](https://github.com/kusold/Shreddit/commit/9b6e57fa14f56138316600be0f46b5791c470f58))
* **ci:** change matchDatasources to matchManagers in renovate.json ([df59e8c](https://github.com/kusold/Shreddit/commit/df59e8cf4cad6242733869732b082a7b284ed369))
* **deps:** bump actions/checkout from 5 to 6 ([a9e3017](https://github.com/kusold/Shreddit/commit/a9e30172b1325a4c58dad2f47bcbe54f930f71ae))
* **deps:** bump actions/download-artifact from 4 to 6 ([17c2932](https://github.com/kusold/Shreddit/commit/17c2932f87cec1f5798ca809247fbf3fe6d72af8))
* **deps:** bump actions/download-artifact from 6 to 7 ([4e1bf45](https://github.com/kusold/Shreddit/commit/4e1bf45ff25c2611c081e3a5eaa176bf4f756ae5))
* **deps:** bump actions/download-artifact from 7 to 8 ([9a78b38](https://github.com/kusold/Shreddit/commit/9a78b3844410253fa5450508ff10ec7183813e5c))
* **deps:** bump actions/github-script from 7 to 8 ([99adb09](https://github.com/kusold/Shreddit/commit/99adb09ba749de70e873c368903095a82b3e8878))
* **deps:** bump actions/setup-python from 5 to 6 ([7d3977c](https://github.com/kusold/Shreddit/commit/7d3977c922018e51d6f8c4240d8eb6d3efebd68b))
* **deps:** bump actions/upload-artifact from 4 to 5 ([d6c0f14](https://github.com/kusold/Shreddit/commit/d6c0f149f7f6c24f4a163bd76288c474cb1de74d))
* **deps:** bump actions/upload-artifact from 5 to 6 ([63c464f](https://github.com/kusold/Shreddit/commit/63c464fcfddab388b404b8cc137dfb518fcd69a6))
* **deps:** bump actions/upload-artifact from 6 to 7 ([9bb3285](https://github.com/kusold/Shreddit/commit/9bb32851bcb7552c9a754b718d4f30f990d79959))
* **deps:** bump cycjimmy/semantic-release-action from 4 to 5 ([a9871be](https://github.com/kusold/Shreddit/commit/a9871beddfb1fb3458d0a179321f427fb5cd30ad))
* **deps:** bump cycjimmy/semantic-release-action from 5.0.2 to 6.0.0 ([6dd5941](https://github.com/kusold/Shreddit/commit/6dd59419b09d6cbb5cfc7157354fb5bc0f4aaf0d))
* **deps:** bump docker/build-push-action from 6 to 7 ([82c78ce](https://github.com/kusold/Shreddit/commit/82c78ce63230047485b5329a09beebd8a434b82b))
* **deps:** bump docker/login-action from 3 to 4 ([6a941e4](https://github.com/kusold/Shreddit/commit/6a941e41b219044867280fcb34160b38709e7ba2))
* **deps:** bump docker/metadata-action from 5 to 6 ([b909f83](https://github.com/kusold/Shreddit/commit/b909f8357182c2b90643577bde92d254826bf63c))
* **deps:** bump docker/setup-buildx-action from 3 to 4 ([8e39072](https://github.com/kusold/Shreddit/commit/8e390724d45fc0e389dbea56af7b8da17d701311))
* **deps:** bump github/codeql-action from 3 to 4 ([16744b2](https://github.com/kusold/Shreddit/commit/16744b251ea9e8b7f328574e8763046a6fb6fd29))
* **deps:** bump pygments from 2.19.2 to 2.20.0 ([3ef539a](https://github.com/kusold/Shreddit/commit/3ef539ab9099b3b3be6a12ee533c03cd10f3c799))
* **deps:** bump requests from 2.32.5 to 2.33.0 ([3e8bcd8](https://github.com/kusold/Shreddit/commit/3e8bcd886bc12c48b6c6f6c69f15c3b111531db7))
* **deps:** bump tornado from 6.5.2 to 6.5.5 ([b22a963](https://github.com/kusold/Shreddit/commit/b22a96347b63059712e9d968b4143fca287ec4c3))
* **deps:** bump urllib3 from 2.5.0 to 2.6.3 ([576ca3f](https://github.com/kusold/Shreddit/commit/576ca3f0c7a1234157199818f51732d6ba8f4f46))
* **deps:** pin dependencies ([6082802](https://github.com/kusold/Shreddit/commit/6082802f28885bd8a7c2baa0e33e6096bf878aac))
* **deps:** renovate config — semantic commits, labels, pin github-actions, automerge minor+ ([5faf6d6](https://github.com/kusold/Shreddit/commit/5faf6d6615a9be28057bb81402286670d2bb113f))
* **deps:** update actions/checkout action to v5 ([48154fb](https://github.com/kusold/Shreddit/commit/48154fb5075873387f880ce5510026ec46e80167))
* **deps:** update actions/checkout action to v5.0.1 ([#207](https://github.com/kusold/Shreddit/issues/207)) ([d224efb](https://github.com/kusold/Shreddit/commit/d224efb59f1e3a9e02a7658877dde09a382352e7))
* **deps:** update actions/dependency-review-action action to v4.8.2 ([#196](https://github.com/kusold/Shreddit/issues/196)) ([9af1de5](https://github.com/kusold/Shreddit/commit/9af1de59ad48f8734378e5e193b56aef44b3f701))
* **deps:** update actions/dependency-review-action action to v4.8.3 ([#222](https://github.com/kusold/Shreddit/issues/222)) ([ba60e44](https://github.com/kusold/Shreddit/commit/ba60e4427add1f9fe0c56a364de926ae3d73a7aa))
* **deps:** update actions/dependency-review-action action to v4.9.0 ([#227](https://github.com/kusold/Shreddit/issues/227)) ([994fcaf](https://github.com/kusold/Shreddit/commit/994fcaffbc56601262613ad89f8a85ac0d2108c7))
* **deps:** update actions/setup-node action to v6 ([e6af6dd](https://github.com/kusold/Shreddit/commit/e6af6dd40e882ea834770ed7e200071de49cc37d))
* **deps:** update amannn/action-semantic-pull-request action to v6 ([af4a16c](https://github.com/kusold/Shreddit/commit/af4a16c7d6edd59135e2fb4f6a90b8cf86d7a8b0))
* **deps:** update astral-sh/setup-uv action to v7 ([96797d7](https://github.com/kusold/Shreddit/commit/96797d75dcdccd73ebdcd2eda82c0955e092b265))
* **deps:** update cycjimmy/semantic-release-action action to v5.0.2 ([#206](https://github.com/kusold/Shreddit/issues/206)) ([8c8347f](https://github.com/kusold/Shreddit/commit/8c8347f5bf4f68af1824e3386c4e9b92f26bba65))
* **deps:** update dependency node to v24 ([3dc2802](https://github.com/kusold/Shreddit/commit/3dc2802d7e5ed4e7aada7bd0b7da5edae7207c9a))
* **deps:** update dependency node to v24.12.0 ([#214](https://github.com/kusold/Shreddit/issues/214)) ([d31a06e](https://github.com/kusold/Shreddit/commit/d31a06e55ba408efe48d3600ac195f8071f8f279))
* **deps:** update dependency node to v24.13.0 ([#216](https://github.com/kusold/Shreddit/issues/216)) ([2b2e97c](https://github.com/kusold/Shreddit/commit/2b2e97ca556d9d26f608bed6026f4fed5b409ceb))
* **deps:** update dependency node to v24.13.1 ([#220](https://github.com/kusold/Shreddit/issues/220)) ([1d79820](https://github.com/kusold/Shreddit/commit/1d79820957f4dd2a15a063659299f62fc3df4730))
* **deps:** update dependency node to v24.14.0 ([#223](https://github.com/kusold/Shreddit/issues/223)) ([3c8deb2](https://github.com/kusold/Shreddit/commit/3c8deb22833f6a54758659297cf93d95ce86363f))
* **deps:** update dependency node to v24.14.1 ([#238](https://github.com/kusold/Shreddit/issues/238)) ([ded2b6d](https://github.com/kusold/Shreddit/commit/ded2b6dfb142e604b8a855368b9cb03e2114366a))
* **deps:** update dependency python to v3.14.1 ([#210](https://github.com/kusold/Shreddit/issues/210)) ([e32b494](https://github.com/kusold/Shreddit/commit/e32b494377f26fd3b5ee803b9243ba68238154bf))
* **deps:** update dependency python to v3.14.2 ([#211](https://github.com/kusold/Shreddit/issues/211)) ([4528ffa](https://github.com/kusold/Shreddit/commit/4528ffa5a9f110e28fa55627da64425c2e007d05))
* **deps:** update dependency python to v3.14.3 ([#219](https://github.com/kusold/Shreddit/issues/219)) ([f1e8640](https://github.com/kusold/Shreddit/commit/f1e8640d99144add59729213a8f50059b7da6806))
* **deps:** update sigstore/cosign-installer action to v4.1.0 ([#235](https://github.com/kusold/Shreddit/issues/235)) ([e7ca0a9](https://github.com/kusold/Shreddit/commit/e7ca0a9fdd0feec64b0ed18a5c3145bfb45fdd1d))
* **deps:** update sigstore/cosign-installer action to v4.1.1 ([#240](https://github.com/kusold/Shreddit/issues/240)) ([4ce25e5](https://github.com/kusold/Shreddit/commit/4ce25e50e54f7ea21ec27283e52c44a1fdf1b642))

## [6.4.1](https://github.com/kusold/Shreddit/compare/v6.4.0...v6.4.1) (2025-11-02)

### Bug Fixes

* correct semantic-release branch config and remove redundant ruff target-version ([e52007c](https://github.com/kusold/Shreddit/commit/e52007c10f2eda4e10a5f4d6534036b51b9acce3))

### Chores

* update workflows to use main branch instead of master ([06885ad](https://github.com/kusold/Shreddit/commit/06885ada4a69cdb675665278b7451c072cfb5677))

## [6.4.0](https://github.com/kusold/Shreddit/compare/v6.3.2...v6.4.0) (2025-11-02)

### Features

* **lint:** add ruff linter with CI integration and auto-fixes ([939aeba](https://github.com/kusold/Shreddit/commit/939aeba142f5d64814dfdf76eabb9175a4722af5))

### Bug Fixes

* update test workflow to use virtual environment and add Python 3.14 ([dffa0ff](https://github.com/kusold/Shreddit/commit/dffa0ff971ef74d7810d568824f548d835e567c0))

### Documentation

* add PR description update requirement to agent workflow ([343d913](https://github.com/kusold/Shreddit/commit/343d913b8317498589f83f4ac4056b7b054cc32f))
* add test requirement before commits in AGENTS.md ([a61dd3e](https://github.com/kusold/Shreddit/commit/a61dd3e7fdf13eef0c9c8b066f8d2436338f355a))
* clarify repository history in README callout ([3713d24](https://github.com/kusold/Shreddit/commit/3713d24f215a26ad3b5f7f0d5a3bc171ef864d7c))

### Code Refactoring

* **lint:** eliminate all global ruff ignores and extract magic value constant ([00c9150](https://github.com/kusold/Shreddit/commit/00c9150c051581b71404aa867594a7c71b3f10c6))

### Chores

* remove legacy packaging files and add test suite ([5ddccde](https://github.com/kusold/Shreddit/commit/5ddccde84a769debc682f6746f61551a50265765))

## [6.3.2](https://github.com/kusold/Shreddit/compare/v6.3.1...v6.3.2) (2025-11-02)

### Documentation

* add PR workflow requirements to AGENTS.md ([7fea88e](https://github.com/kusold/Shreddit/commit/7fea88ecff6aa6facbf072991a882e2d33849b36))

## [6.3.1](https://github.com/kusold/Shreddit/compare/v6.3.0...v6.3.1) (2025-11-02)

### Bug Fixes

* bump idna from 2.5 to 3.7 to resolve CVE-2024-3651 ([3718d94](https://github.com/kusold/Shreddit/commit/3718d949afaba8ac80bdcf200b961683352cfb6d)), closes [#91](https://github.com/kusold/Shreddit/issues/91)

### Documentation

* add AGENTS.md and update documentation for Python 3.12+ requirement ([f28cb49](https://github.com/kusold/Shreddit/commit/f28cb497ebf12b3b602e24a26d42aa87229770a8))

### Chores

* improve semantic-pr workflow documentation ([7d2a8ab](https://github.com/kusold/Shreddit/commit/7d2a8ab37db67f8be5748184b98c05110acf3352))

## [6.3.0](https://github.com/kusold/Shreddit/compare/v6.2.0...v6.3.0) (2025-11-02)

### Features

* add automated Docker security scanning with vulnerability remediation ([c06074d](https://github.com/kusold/Shreddit/commit/c06074dd32014109302cf73369aea2e0066a79fc))
* add semantic commit validation and improve vulnerability scanning ([b406878](https://github.com/kusold/Shreddit/commit/b406878fd872855478318487366ddede02e4caa6))

### Chores

* add commitlint configuration file ([c74b30e](https://github.com/kusold/Shreddit/commit/c74b30e750b57d3bb73b747909172e959c288588))

## [6.2.0](https://github.com/kusold/Shreddit/compare/v6.1.0...v6.2.0) (2025-11-02)

### Features

* add automated release workflow with semantic versioning and binary builds ([7a514a2](https://github.com/kusold/Shreddit/commit/7a514a29a3466b7dbf03545ca89d162fb380387f))
* migrate project to use uv for package management ([87f6207](https://github.com/kusold/Shreddit/commit/87f62072ddc4ee8120a1b48214812fd0491c318c))
* upgrade to Python 3.12 and add setuptools dependency ([05bc95b](https://github.com/kusold/Shreddit/commit/05bc95b2bbd59165588907040818d260849ce226))
* upgrade to Python 3.13 ([c19a2e1](https://github.com/kusold/Shreddit/commit/c19a2e174569fbb14069660358d59287039ff476))
* upgrade to Python 3.14 ([cf76248](https://github.com/kusold/Shreddit/commit/cf76248192e6fee033c18ea0bca784491b7d093f))

### Bug Fixes

* add missing appdirs dependency to pyproject.toml ([39c2066](https://github.com/kusold/Shreddit/commit/39c206654ca7f587d20f349bd85248bbad201943))
* include README.md in Dockerfile for build ([53ee142](https://github.com/kusold/Shreddit/commit/53ee1422d7630dfbd6aa8873b4fde088bb581be5))

### Documentation

* add Apple Container instructions for macOS users ([9650e5d](https://github.com/kusold/Shreddit/commit/9650e5d6f3963dd7a7223f9e72145228d1465166))

### Code Refactoring

* switch to official Python image with uv via multi-stage build ([ff5b6ba](https://github.com/kusold/Shreddit/commit/ff5b6ba57e94c81c1129ed5916b320772dc4765b))
