# Winback and Reactivation Playbook - Dorje Teas D2C Revenue Growth OS

> Public-information based winback playbook. No internal Dorje lifecycle data used.
> Thresholds are [SYNTHETIC] planning assumptions.

## Winback Segment Definitions

| Segment | Definition | Primary Product Path |
|---|---|---|
| Bought once, no return in 60+ days | First order only, no second order | Product-specific replenishment or adjacent product |
| Bought twice, no return in 45+ days | Demonstrated trust but habit stalled | Tea Club or replenishment prompt |
| Gift Buyer, no self-purchase in 45+ days | Bought Selim Hill Gift Box Classic or Premium, no own-use order | Soft self-purchase path |
| High-AOV dormant customer | Premium seasonal or gift buyer, no activity | Harvest or estate update |
| Lapsed subscriber | Cancelled or paused Tea Club | Cadence reset or product rotation |

## Two-Message Sequence by Segment

| Segment | Message 1: Soft, No Discount | Message 2: Modest Segment-Specific Offer |
|---|---|---|
| Bought once, no return in 60+ days | Brewing confidence and product-specific reminder | Free shipping on same product or adjacent product |
| Bought twice, no return in 45+ days | "Your usual tea may be running low" | Small replenishment discount with expiry |
| Gift Buyer, no self-purchase in 45+ days | "You gifted Dorje. Try the same story for yourself." | Free shipping on Original Darjeeling Chai or First Flush Darjeeling |
| High-AOV dormant customer | Estate or harvest update | Early access to First Flush Darjeeling or Second Flush Darjeeling |
| Lapsed subscriber | "Pause, switch cadence, or rotate product" | Reactivation with better cadence, not heavy discount |

## Offer Logic

| Offer | Use When | Avoid When |
|---|---|---|
| Free shipping | Buyer is near AOV threshold or shipping friction is likely | CM is already thin |
| Small discount | Buyer has clear product intent but did not return | Premium positioning is at risk |
| New product introduction | Buyer may need novelty | Buyer has not built trust yet |
| Estate update | Darjeeling Loyalist or Climate/Story-Led Buyer segment | Buyer bought only for gift utility |
| Limited harvest note | First Flush Darjeeling or Second Flush Darjeeling buyers | Stock is constrained |

## Suppression Logic

Do not send winback if:

- Customer purchased in the last 14 days.
- Customer has an unresolved delivery issue.
- Customer cancelled because of product quality and has not received service recovery.
- Customer is currently in a subscription pause window.
- Customer already received two winback offers in 90 days [SYNTHETIC].

## Seasonal Retry Logic

| Season | Retry Audience | Message |
|---|---|---|
| March-April | Dormant Darjeeling Loyalist | First Flush Darjeeling harvest update |
| May-June | First Flush Darjeeling buyer | Second Flush Darjeeling continuation |
| September-October | Dormant Gift Buyer | Selim Hill Gift Box Classic and Selim Hill Gift Box Premium planning reminder |
| December-January | Dormant Daily Premium Tea Drinker | Original Darjeeling Chai winter ritual |

## Reactivation Metrics

| Metric | Decision Use |
|---|---|
| Reactivation rate | Shows whether segment is worth repeated effort |
| Revenue per winback send | Prevents sending low-quality volume |
| Contribution margin per reactivated order | Prevents discount-led unprofitable recovery |
| Time from winback to purchase | Helps tune urgency and timing |
| Repeat after reactivation | Separates true reactivation from one-off discount purchase |

## Contribution Margin Logic

Winback should not use discounts that erase margin. If the second message requires an offer, start with free shipping or product education before discount. A winback order that is revenue-positive but contribution-margin-negative should be treated as a failed winback unless it leads to repeat CM-positive behavior.
