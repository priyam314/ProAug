ENV := default
help:
	@echo "\033[92m######## HELP ########\033[0m"
	@echo "\033[91mmake help\033[0m"
	@echo "\033[91mmake setup\033[0m"

setup:
	@echo "\033[92mIf working on notebook, restart after augly library is installed\033[0m"
	@echo "\033[93m\033[1mIntalling augly\033[0m"
	case "$(ENV)" in "notebook") pip3 install -U augly;; \
	"default") pip3 install -U augly;; \
	esac

	@echo "\033[93m\033[1mInstalling python3-magic\033[0m"
	case "$(ENV)" in "notebook") sudo apt-get install python3-magic;; \
	"default") sudo apt-get install python3-magic;; \
	esac

	@echo "\033[93m\033[1mInstalling requirements\033[0m"
	case "$(ENV)" in "notebook") pip3 install -r requirements.txt;; \
	"default") pip3 install -r requirements.txt;; \
	esac

clean:
	@echo "\033[92m\033[1mCleaning up unwanted files and folders\033[0m"
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr
	rm -fr docs/_build/
	@echo "\033[91m\033[1mCleaning finished\033[0m"
