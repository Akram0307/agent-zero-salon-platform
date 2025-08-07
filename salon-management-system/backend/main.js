const { OrchestrationAgent } = require('./src/orchestrator');

// Initialize the orchestrator
const orchestrator = new OrchestrationAgent();

// Example usage
async function main() {
  console.log('Salon Management AI Agents System');
  console.log('Initializing agents...');

  try {
    // Example task routing
    const exampleTasks = [
      {
        type: 'booking',
        description: 'Customer wants to book a haircut appointment',
        context: {
          customerName: 'John Doe',
          preferredDateTime: '2025-08-10 14:00',
          serviceType: 'haircut'
        }
      },
      {
        type: 'pricing',
        description: 'Determine dynamic pricing for peak hours',
        context: {
          dateTime: '2025-08-10 18:00',
          serviceType: 'coloring',
          demandLevel: 'high'
        }
      },
      {
        type: 'churn-risk',
        description: 'Assess churn risk for customer with declining visits',
        context: {
          customerId: '12345',
          visitHistory: ["2025-01-15", "2025-02-20", "2025-04-10"],
          lastVisit: '2025-04-10'
        }
      }
    ];

    for (const task of exampleTasks) {
      console.log(`
Executing task of type: ${task.type}`);
      try {
        const result = await orchestrator.execute(task);
        console.log(`Result: ${result}`);
      } catch (error) {
        console.error(`Error executing task:`, error.message);
      }
    }

    console.log('
All agents initialized and ready to process tasks.');
  } catch (error) {
    console.error('Error initializing agents:', error);
  }
}

// Run the main function if this file is executed directly
if (require.main === module) {
  main();
}

module.exports = { orchestrator };
