const BaseAgent = require('../base-agent');

class ServiceRecommendationAgent extends BaseAgent {
  constructor() {
    super('service recommendation agent');
  }

  async execute(task) {
    // Implement agent-specific logic here
    const prompt = `You are a salon service recommendation agent. Task: ${task.description}. Context: ${JSON.stringify(task.context)}`;
    return await this.generateResponse(prompt);
  }
}

module.exports = ServiceRecommendationAgent;
