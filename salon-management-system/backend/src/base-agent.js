const { VertexAI } = require('@google-cloud/vertexai');
const fs = require('fs');
const path = require('path');

// Load configuration
const configPath = path.join(__dirname, '../config.json');
const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));

class BaseAgent {
  constructor(agentName) {
    this.agentName = agentName;
    this.projectId = config.projectId;
    this.location = config.location;
    this.modelName = config.model;

    // Initialize Vertex AI
    this.vertexAI = new VertexAI({
      project: this.projectId,
      location: this.location,
    });

    // Initialize Gemini model
    this.model = this.vertexAI.getGenerativeModel({
      model: this.modelName,
    });
  }

  async generateResponse(prompt) {
    try {
      const resp = await this.model.generateContent(prompt);
      const contentResponse = await resp.response;
      return contentResponse.candidates[0].content.parts[0].text;
    } catch (error) {
      console.error(`Error in ${this.agentName}:`, error);
      throw error;
    }
  }

  async execute(task) {
    throw new Error('Execute method must be implemented by subclass');
  }
}

module.exports = BaseAgent;
