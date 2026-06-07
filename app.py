from ext import app


if __name__ == "__main__":
    from routes import *
    app.run(debug=True) # debug=True -> ცვლილებების შემთხვევაში აღარ გვიწევს სერვერის თავიდან გაშვება, ავტომატურად აფდეითდება საიტი