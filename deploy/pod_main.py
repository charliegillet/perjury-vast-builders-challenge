"""Pod entrypoint, shipped as /code/main.py so the deploy-app-no-registry command `python main.py` works."""
from app.main import main

if __name__ == "__main__":
    main()
