# Makefile for amdgpu_top COPR package

SPEC_FILE = amdgpu_top.spec
PACKAGE_NAME = amdgpu_top
VERSION = 0.10.5
PROJECT_NAME = amdgpu_top

.PHONY: copr-build copr-build-version copr-status copr-webhook

# Build from GitHub releases
copr-build:
	copr-cli build $(PROJECT_NAME) \
		https://github.com/Umio-Yasuno/amdgpu_top/archive/v$(VERSION).tar.gz

# Build latest from GitHub releases  
copr-build-latest:
	copr-cli build $(PROJECT_NAME) \
		https://github.com/Umio-Yasuno/amdgpu_top/archive/v$(VERSION).tar.gz

# Check build status
copr-status:
	copr-cli list-builds $(PROJECT_NAME)

# Setup SCM package for webhooks
copr-setup-scm:
	copr-cli add-package-scm $(PROJECT_NAME) \
		--name amdgpu_top \
		--clone-url https://github.com/perosredo/amdgpu_top-packaging.git \
		--spec $(SPEC_FILE) \
		--method rpkg \
		--webhook-rebuild on

# Get webhook URL for GitHub setup
copr-webhook:
	@echo "After creating the SCM package, go to:"
	@echo "https://copr.fedorainfracloud.org/coprs/perosredo/$(PROJECT_NAME)/"
	@echo "Then Settings > Integrations to get your webhook URL"
	@echo ""
	@echo "Add this webhook to GitHub at:"
	@echo "https://github.com/Umio-Yasuno/amdgpu_top/settings/hooks"
	@echo "- Payload URL: (from COPR integrations page)"
	@echo "- Content type: application/json"
	@echo "- Events: Release published"