# AI Prompts for Campaign Postmortems - Dorje Teas D2C Revenue Growth OS

> These prompts use pasted campaign data only. They do not imply access to live ad accounts.

## Prompt 1: Single Campaign Postmortem

**Required inputs:** Campaign objective, dates, spend, impressions, clicks, CTR, sessions, orders, revenue, CAC, ROAS, contribution ROAS, product, landing page, audience, creative notes.

```text
You are writing a campaign postmortem for one Dorje Teas D2C campaign.

Data boundary:
- Use only pasted data.
- Do not overstate attribution.
- Do not claim access to live ad account or Shopify data.

Input:
[PASTE DATA HERE]

Analysis instructions:
1. Evaluate intent quality using CTR and search/audience context.
2. Evaluate conversion quality using CVR and landing page match.
3. Evaluate economics using CAC, ROAS, and contribution ROAS.
4. Identify whether the product was matched to the right segment.
5. Decide whether the campaign should Scale, Fix, Kill, or Run again next season.

Output format:
1. Campaign summary
2. What worked
3. What failed
4. Economics read
5. Decision: Scale / Fix / Kill / Run again next season
6. Next action

Attribution warning:
Do not treat reported ROAS as complete truth. State what additional attribution or order-level data would improve confidence.
```

## Prompt 2: Multi-Campaign Comparison

**Required inputs:** Campaign table with campaign_id, campaign_name, platform, spend, revenue, CAC, ROAS, contribution ROAS, CTR, CVR, orders, product, landing page, dates.

```text
Compare the Dorje Teas campaigns below and recommend budget allocation.

Input:
[PASTE DATA HERE]

Analysis instructions:
1. Rank campaigns by contribution ROAS, not ROAS alone.
2. Identify campaigns with strong CTR but weak CVR.
3. Identify campaigns with acceptable revenue but weak contribution margin.
4. Separate seasonal First Flush Darjeeling or gifting campaigns from always-on daily tea campaigns.
5. Recommend Scale, Fix, Kill, or Run again next season for each campaign.

Output format:
| Campaign | Read | Decision | Reason | Next Action |

Decision options:
- Scale
- Fix
- Kill
- Run again next season

Attribution warning:
Do not overinterpret platform attribution. Mention whether the decision depends on Shopify order reconciliation, incrementality, or cohort repeat behavior.
```
