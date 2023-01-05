from app import create_app
import config


app = create_app(config.DevelopmentConfig)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
