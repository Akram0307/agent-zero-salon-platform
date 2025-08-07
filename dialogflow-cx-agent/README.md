# Dialogflow CX Agent for Salon Management System

This directory contains the configuration files for the Dialogflow CX agent used in the salon management system.

## Structure

- `intents/` - Contains intent definitions
- `entities/` - Contains entity definitions
- `webhooks/` - Contains webhook configurations
- `flows/` - Contains flow definitions

## Intents

1. **Booking Service** - Handles new booking requests
2. **Reschedule Booking** - Handles rescheduling existing bookings
3. **Cancel Booking** - Handles canceling existing bookings
4. **Salon Information** - Provides general salon information

## Entities

1. **service-type** - Types of services offered (haircut, manicure, etc.)
2. **date** - Date expressions (today, tomorrow, etc.)
3. **time** - Time expressions (morning, afternoon, etc.)
4. **customer-name** - Customer name entity
5. **phone-number** - Phone number entity (regexp-based)

## Webhooks

1. **Booking Webhook** - Calls the booking service API to create new bookings
2. **Reschedule Webhook** - Calls the booking service API to reschedule bookings
3. **Cancel Webhook** - Calls the booking service API to cancel bookings
4. **Info Webhook** - Calls the booking service API to get salon information

## Deployment

To deploy this agent to Dialogflow CX:

1. Create a new Dialogflow CX agent in the Google Cloud Console
2. Update the PROJECT_ID, LOCATION_ID, and AGENT_ID in all JSON files
3. Upload the intents, entities, webhooks, and flows using the Dialogflow CX API or Console

## Integration

The agent integrates with the core API endpoints:

- POST /api/bookings - Create new bookings
- POST /api/bookings/reschedule - Reschedule existing bookings
- POST /api/bookings/cancel - Cancel existing bookings
- GET /api/salon/info - Get salon information

All endpoints require an API key in the x-api-key header.
