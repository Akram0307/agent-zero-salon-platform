const BaseAgent = require('../base-agent');

class UpsellCrossSellAgent extends BaseAgent {
  constructor() {
    super('upsell cross sell agent');
  }

  async execute(task) {
    // Implement agent-specific logic here
    const prompt = `You are a salon upsell cross sell agent. Task: ${task.description}. Context: ${JSON.stringify(task.context)}`;
    return await this.generateResponse(prompt);
  }
}

module.exports = UpsellCrossSellAgent;
