const BaseAgent = require('../base-agent');

class LoyaltyProgramAgent extends BaseAgent {
  constructor() {
    super('loyalty program agent');
  }

  async execute(task) {
    // Implement agent-specific logic here
    const prompt = `You are a salon loyalty program agent. Task: ${task.description}. Context: ${JSON.stringify(task.context)}`;
    return await this.generateResponse(prompt);
  }
}

module.exports = LoyaltyProgramAgent;
