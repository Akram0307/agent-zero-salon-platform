const BaseAgent = require('../base-agent');

class ReviewRequestAgent extends BaseAgent {
  constructor() {
    super('review request agent');
  }

  async execute(task) {
    // Implement agent-specific logic here
    const prompt = `You are a salon review request agent. Task: ${task.description}. Context: ${JSON.stringify(task.context)}`;
    return await this.generateResponse(prompt);
  }
}

module.exports = ReviewRequestAgent;
