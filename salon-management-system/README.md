# Salon Management AI Agents System

This is a multi-agent AI system for salon management built with Vertex AI's Gemini models. The system consists of 21 specialized AI agents organized into 5 functional categories.

## Architecture

The system follows a multi-agent architecture where each agent is responsible for a specific domain of salon operations. All agents are implemented using Vertex AI's Gemini models and are coordinated by an orchestration agent.

## Agent Categories

### 1. Core Customer & Booking Agents
- **Conversational Booking Agent**: Handles customer appointment bookings through natural language conversations
- **Stylist Assignment Agent**: Assigns customers to appropriate stylists based on expertise and availability
- **Appointment Modification Agent**: Manages changes to existing appointments
- **Service Recommendation Agent**: Recommends services based on customer preferences and history

### 2. Revenue & Marketing Agents
- **Dynamic Pricing Agent**: Adjusts service pricing based on demand, time, and other factors
- **Personalized Offers Agent**: Creates customized offers for individual customers
- **Ad Campaign Agent**: Designs and manages marketing campaigns
- **Upsell/Cross-sell Agent**: Identifies opportunities to increase sales through additional services

### 3. Customer Retention Agents
- **LTV Forecasting Agent**: Predicts customer lifetime value
- **Churn Risk Agent**: Identifies customers at risk of not returning
- **Loyalty Program Agent**: Manages customer loyalty programs
- **Review Request Agent**: Requests reviews from customers after services

### 4. Operational Agents
- **Staff Productivity Agent**: Monitors and optimizes staff performance
- **Inventory Management Agent**: Tracks and manages salon inventory
- **Financial Reconciliation Agent**: Handles financial tracking and reconciliation
- **Waitlist Management Agent**: Manages customer waitlists

### 5. System Management Agents
- **Orchestration Agent**: Coordinates all other agents and routes tasks appropriately
- **Safety & Compliance Agent**: Ensures operations meet safety and compliance requirements
- **Data Quality Agent**: Monitors and maintains data quality
- **Performance Monitoring Agent**: Tracks system performance and identifies issues
- **Error Handling Agent**: Manages error detection and recovery

## Implementation Details

All agents are implemented using the Vertex AI SDK for Node.js with Gemini models. Each agent extends a base agent class that provides common functionality for interacting with the Vertex AI API.

## How to Run

1. Install dependencies:
   ```
   npm install
   ```

2. Run the system:
   ```
   npm start
   ```

## Configuration

The system requires a `config.json` file in the backend directory with the following structure:

```json
{
  "projectId": "your-gcp-project-id",
  "location": "us-central1",
  "model": "gemini-1.5-pro-001"
}
```

## Usage Example

```javascript
const { OrchestrationAgent } = require('./backend/src/orchestrator');

const orchestrator = new OrchestrationAgent();

const task = {
  type: 'booking',
  description: 'Customer wants to book a haircut appointment',
  context: {
    customerName: 'John Doe',
    preferredDateTime: '2025-08-10 14:00',
    serviceType: 'haircut'
  }
};

const result = await orchestrator.execute(task);
```
