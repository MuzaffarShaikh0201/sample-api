import uvicorn
import argparse

from .main import app


def dev_mode():
    uvicorn.run("src.main:app", port=5000, use_colors=True, reload=True)


def prod_mode():
    uvicorn.run(app, host="0.0.0.0", port=5000, use_colors=True)


def run_sample_api():
    parser = argparse.ArgumentParser(description="Run the Sample API.")
    parser.add_argument(
        "--mode",
        choices=["dev", "prod"],
        required=True,
        help="Mode to run the API (dev or prod).",
    )
    args = parser.parse_args()

    mode = args.mode
    if mode == "dev":
        print("Running in development mode...")
        dev_mode()
    elif mode == "prod":
        print("Running in production mode...")
        prod_mode()
