from app import create_app

app = create_app()

# Define a root route for the app
@app.route("/")
def home():
    return "Welcome to the Multi-Utility App!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


