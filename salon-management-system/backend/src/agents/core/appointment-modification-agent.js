const BaseAgent = require('../base-agent');

class AppointmentModificationAgent extends BaseAgent {
  constructor() {
    super('appointment modification agent');
  }

  async execute(task) {
    // Implement agent-specific logic here
    const prompt = `You are a salon appointment modification agent. Task: ${task.description}. Context: ${JSON.stringify(task.context)}`;
    return await this.generateResponse(prompt);
  }
}

module.exports = AppointmentModificationAgent;
