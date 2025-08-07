const BaseAgent = require('../base-agent');

class ConversationalBookingAgent extends BaseAgent {
  constructor() {
    super('conversational booking agent');
  }

  async execute(task) {
    // Implement agent-specific logic here
    const prompt = `You are a salon conversational booking agent. Task: ${task.description}. Context: ${JSON.stringify(task.context)}`;
    return await this.generateResponse(prompt);
  }
}

module.exports = ConversationalBookingAgent;
