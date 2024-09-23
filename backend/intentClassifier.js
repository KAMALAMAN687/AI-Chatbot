const { spawn } = require("child_process");
const path = require("path");

function classifyIntent(userMessage) {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("python", [
      path.join(__dirname, "../nlp", "intentClassifier.py"),
      userMessage,
    ]);

    pythonProcess.stdout.on("data", (data) => {
      resolve(data.toString());
    });

    pythonProcess.stderr.on("data", (data) => {
      reject(data.toString());
    });
  });
}

module.exports = { classifyIntent };
