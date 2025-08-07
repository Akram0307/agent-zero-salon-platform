// Export all agents

// Core agents
exports.ConversationalBookingAgent = require('./agents/core/conversational-booking-agent');
exports.StylistAssignmentAgent = require('./agents/core/stylist-assignment-agent');
exports.AppointmentModificationAgent = require('./agents/core/appointment-modification-agent');
exports.ServiceRecommendationAgent = require('./agents/core/service-recommendation-agent');

// Revenue & Marketing agents
exports.DynamicPricingAgent = require('./agents/revenue/dynamic-pricing-agent');
exports.PersonalizedOffersAgent = require('./agents/revenue/personalized-offers-agent');
exports.AdCampaignAgent = require('./agents/revenue/ad-campaign-agent');
exports.UpsellCrossSellAgent = require('./agents/revenue/upsell-cross-sell-agent');

// Customer Retention agents
exports.LTVForecastingAgent = require('./agents/customer/ltv-forecasting-agent');
exports.ChurnRiskAgent = require('./agents/customer/churn-risk-agent');
exports.LoyaltyProgramAgent = require('./agents/customer/loyalty-program-agent');
exports.ReviewRequestAgent = require('./agents/customer/review-request-agent');

// Operational agents
exports.StaffProductivityAgent = require('./agents/operational/staff-productivity-agent');
exports.InventoryManagementAgent = require('./agents/operational/inventory-management-agent');
exports.FinancialReconciliationAgent = require('./agents/operational/financial-reconciliation-agent');
exports.WaitlistManagementAgent = require('./agents/operational/waitlist-management-agent');

// System Management agents
exports.OrchestrationAgent = require('./agents/system/orchestration-agent');
exports.SafetyComplianceAgent = require('./agents/system/safety-compliance-agent');
exports.DataQualityAgent = require('./agents/system/data-quality-agent');
exports.PerformanceMonitoringAgent = require('./agents/system/performance-monitoring-agent');
exports.ErrorHandlingAgent = require('./agents/system/error-handling-agent');
