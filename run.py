from app import create_app

app = create_app()

if __name__ == "__main__":
    # Run on 0.0.0.0 and port 8080 (required by App Runner)
    app.run(host="0.0.0.0", port=8080)
