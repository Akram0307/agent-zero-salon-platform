const BaseAgent = require('./base-agent');

// Import all agents
class OrchestrationAgent extends BaseAgent {
  constructor() {
    super('orchestration-agent');
    this.agents = {};
  }

  async initializeAgents() {
    // Core agents
    const { ConversationalBookingAgent } = require('./agents/core/conversational-booking-agent');
    const { StylistAssignmentAgent } = require('./agents/core/stylist-assignment-agent');
    const { AppointmentModificationAgent } = require('./agents/core/appointment-modification-agent');
    const { ServiceRecommendationAgent } = require('./agents/core/service-recommendation-agent');

    // Revenue & Marketing agents
    const { DynamicPricingAgent } = require('./agents/revenue/dynamic-pricing-agent');
    const { PersonalizedOffersAgent } = require('./agents/revenue/personalized-offers-agent');
    const { AdCampaignAgent } = require('./agents/revenue/ad-campaign-agent');
    const { UpsellCrossSellAgent } = require('./agents/revenue/upsell-cross-sell-agent');

    // Customer Retention agents
    const { LTVForecastingAgent } = require('./agents/customer/ltv-forecasting-agent');
    const { ChurnRiskAgent } = require('./agents/customer/churn-risk-agent');
    const { LoyaltyProgramAgent } = require('./agents/customer/loyalty-program-agent');
    const { ReviewRequestAgent } = require('./agents/customer/review-request-agent');

    // Operational agents
    const { StaffProductivityAgent } = require('./agents/operational/staff-productivity-agent');
    const { InventoryManagementAgent } = require('./agents/operational/inventory-management-agent');
    const { FinancialReconciliationAgent } = require('./agents/operational/financial-reconciliation-agent');
    const { WaitlistManagementAgent } = require('./agents/operational/waitlist-management-agent');

    // System Management agents
    const { SafetyComplianceAgent } = require('./agents/system/safety-compliance-agent');
    const { DataQualityAgent } = require('./agents/system/data-quality-agent');
    const { PerformanceMonitoringAgent } = require('./agents/system/performance-monitoring-agent');
    const { ErrorHandlingAgent } = require('./agents/system/error-handling-agent');

    // Initialize agents
    this.agents = {
      // Core agents
      conversationalBooking: new ConversationalBookingAgent(),
      stylistAssignment: new StylistAssignmentAgent(),
      appointmentModification: new AppointmentModificationAgent(),
      serviceRecommendation: new ServiceRecommendationAgent(),

      // Revenue & Marketing agents
      dynamicPricing: new DynamicPricingAgent(),
      personalizedOffers: new PersonalizedOffersAgent(),
      adCampaign: new AdCampaignAgent(),
      upsellCrossSell: new UpsellCrossSellAgent(),

      // Customer Retention agents
      ltvForecasting: new LTVForecastingAgent(),
      churnRisk: new ChurnRiskAgent(),
      loyaltyProgram: new LoyaltyProgramAgent(),
      reviewRequest: new ReviewRequestAgent(),

      // Operational agents
      staffProductivity: new StaffProductivityAgent(),
      inventoryManagement: new InventoryManagementAgent(),
      financialReconciliation: new FinancialReconciliationAgent(),
      waitlistManagement: new WaitlistManagementAgent(),

      // System Management agents
      safetyCompliance: new SafetyComplianceAgent(),
      dataQuality: new DataQualityAgent(),
      performanceMonitoring: new PerformanceMonitoringAgent(),
      errorHandling: new ErrorHandlingAgent()
    };
  }

  async routeTask(task) {
    // Route task to appropriate agent based on task type
    switch(task.type) {
      // Core agents
      case 'booking':
        return await this.agents.conversationalBooking.execute(task);
      case 'stylist-assignment':
        return await this.agents.stylistAssignment.execute(task);
      case 'appointment-modification':
        return await this.agents.appointmentModification.execute(task);
      case 'service-recommendation':
        return await this.agents.serviceRecommendation.execute(task);

      // Revenue & Marketing agents
      case 'pricing':
        return await this.agents.dynamicPricing.execute(task);
      case 'offers':
        return await this.agents.personalizedOffers.execute(task);
      case 'ad-campaign':
        return await this.agents.adCampaign.execute(task);
      case 'upsell':
        return await this.agents.upsellCrossSell.execute(task);

      // Customer Retention agents
      case 'ltv-forecast':
        return await this.agents.ltvForecasting.execute(task);
      case 'churn-risk':
        return await this.agents.churnRisk.execute(task);
      case 'loyalty':
        return await this.agents.loyaltyProgram.execute(task);
      case 'review':
        return await this.agents.reviewRequest.execute(task);

      // Operational agents
      case 'staff-productivity':
        return await this.agents.staffProductivity.execute(task);
      case 'inventory':
        return await this.agents.inventoryManagement.execute(task);
      case 'financial':
        return await this.agents.financialReconciliation.execute(task);
      case 'waitlist':
        return await this.agents.waitlistManagement.execute(task);

      // System Management agents
      case 'safety':
        return await this.agents.safetyCompliance.execute(task);
      case 'data-quality':
        return await this.agents.dataQuality.execute(task);
      case 'monitoring':
        return await this.agents.performanceMonitoring.execute(task);
      case 'error':
        return await this.agents.errorHandling.execute(task);

      default:
        throw new Error(`Unknown task type: ${task.type}`);
    }
  }

  async execute(task) {
    // Initialize agents if not already done
    if (Object.keys(this.agents).length === 0) {
      await this.initializeAgents();
    }

    // Route task to appropriate agent
    return await this.routeTask(task);
  }
}

module.exports = OrchestrationAgent;
