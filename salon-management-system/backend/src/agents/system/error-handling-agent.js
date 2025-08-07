const BaseAgent = require('../base-agent');

class ErrorHandlingAgent extends BaseAgent {
  constructor() {
    super('error handling agent');
  }

  async execute(task) {
    // Implement agent-specific logic here
    const prompt = `You are a salon error handling agent. Task: ${task.description}. Context: ${JSON.stringify(task.context)}`;
    return await this.generateResponse(prompt);
  }
}

module.exports = ErrorHandlingAgent;
