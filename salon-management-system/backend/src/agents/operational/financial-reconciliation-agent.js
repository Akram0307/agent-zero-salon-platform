const BaseAgent = require('../base-agent');

class FinancialReconciliationAgent extends BaseAgent {
  constructor() {
    super('financial reconciliation agent');
  }

  async execute(task) {
    // Implement agent-specific logic here
    const prompt = `You are a salon financial reconciliation agent. Task: ${task.description}. Context: ${JSON.stringify(task.context)}`;
    return await this.generateResponse(prompt);
  }
}

module.exports = FinancialReconciliationAgent;
