pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        MONGO_URI = credentials('MONGO_URI_SECRET')  
        DB_NAME = 'student_db'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                echo '📦 Creating virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv $VENV_DIR
                    ./$VENV_DIR/bin/pip install --upgrade pip
                    ./$VENV_DIR/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests with pytest...'
                sh '''
                    ./$VENV_DIR/bin/pip install pytest
                    ./$VENV_DIR/bin/python -m pytest test_app.py --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Prepare Environment Variables') {
            steps {
                echo '🔐 Writing environment variables to .env file...'
                sh '''
                    echo "MONGO_URI=${MONGO_URI}" > .env
                    echo "DB_NAME=${DB_NAME}" >> .env
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                echo '🚀 Running Flask app in background...'
                sh '''
                    nohup ./$VENV_DIR/bin/python app.py > flask_app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully.'
            emailext(
                subject: "✅ Jenkins Pipeline Success: ${env.JOB_NAME} [#${env.BUILD_NUMBER}]",
                body: """<p>🎉 Your pipeline <b>${env.JOB_NAME}</b> build <b>#${env.BUILD_NUMBER}</b> was successful.</p>
                         <p>🔗 <a href="${env.BUILD_URL}">View Build</a></p>""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: 'vaibhav10799@gmail.com'
            )
        }
        failure {
            echo '❌ Pipeline failed.'
            emailext(
                subject: "❌ Jenkins Pipeline Failed: ${env.JOB_NAME} [#${env.BUILD_NUMBER}]",
                body: """<p>⚠️ Your pipeline <b>${env.JOB_NAME}</b> build <b>#${env.BUILD_NUMBER}</b> has failed.</p>
                         <p>🔍 <a href="${env.BUILD_URL}">View Console Output</a></p>""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: 'vaibhav10799@gmail.com'
            )
        }
    }
}

