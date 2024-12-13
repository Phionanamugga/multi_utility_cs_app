from app import create_app

if __name__ == "__main__":
    # Create the Flask application instance
    app = create_app()

    # Run the application
    app.run(debug=True, host='0.0.0.0', port=8000)
