"""
generate_synthetic_data.py
Dorje Teas — D2C Revenue Growth OS

Generates all synthetic CSV files for the data model layer.
All values are clearly synthetic and illustrative.
No internal Dorje data was used.

Run: python generate_synthetic_data.py
Output: sample_orders.csv, sample_ad_spend.csv,
        sample_product_catalog.csv, sample_customer_cohorts.csv
"""

import csv
import math
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)  # Reproducible output
SCRIPT_DIR = Path(__file__).resolve().parent

# ─────────────────────────────────────────
# 1. PRODUCT CATALOG
# ─────────────────────────────────────────

PRODUCTS = [
    # id, name, category, pack_gm, price, cogs, pkg_std, shipping_blended, ladder_rung, segment, replen_days
    ("SKU-001", "First Flush Darjeeling",         "First Flush",     100, 750,  180, 55, 106, "premium_seasonal",  "Darjeeling Loyalist",   45),
    ("SKU-002", "Second Flush Darjeeling",         "Second Flush",    100, 650,  160, 55, 106, "premium_seasonal",  "Darjeeling Loyalist",   45),
    ("SKU-003", "Original Darjeeling Chai",        "Chai",            100, 399,  110, 55,  90, "daily_replenishment","Daily Premium Tea Drinker", 28),
    ("SKU-004", "Original Darjeeling Chai",        "Chai",            250, 849,  240, 65,  90, "daily_replenishment","Daily Premium Tea Drinker", 60),
    ("SKU-005", "Darjeeling Green Tea",            "Green Tea",       100, 549,  140, 55,  95, "premium_seasonal",  "Health/Wellness Consumer", 35),
    ("SKU-006", "First Flush Green Tea",           "Green Tea",       100, 699,  165, 55, 100, "premium_seasonal",  "Health/Wellness Consumer", 40),
    ("SKU-007", "Darjeeling Pyramid Teabags",      "Pyramid Teabags",  50, 350,   90, 50,  85, "discovery",         "Daily Premium Tea Drinker", 30),
    ("SKU-008", "Cold Brew Darjeeling",            "Cold Brew",       100, 499,  130, 55,  95, "discovery",         "Health/Wellness Consumer", 35),
    ("SKU-009", "Selim Hill Gift Box Classic",     "Gift Box",        200, 1299, 290, 130, 120, "gifting",          "Gift Buyer",            90),
    ("SKU-010", "Selim Hill Gift Box Premium",     "Gift Box",        300, 1999, 420, 180, 130, "gifting",          "Gift Buyer",            90),
    ("SKU-011", "Tea Club Darjeeling Black Monthly", "Subscription",  100, 649, 155, 55,  90, "subscription",     "Daily Premium Tea Drinker", 30),
    ("SKU-012", "Tea Club Darjeeling Green Monthly", "Subscription",  100, 699, 155, 55,  90, "subscription",     "Health/Wellness Consumer", 30),
]

PRODUCT_BY_ID = {p[0]: p for p in PRODUCTS}

GW_FEE_RATE  = 0.02   # 2% payment gateway fee
FREE_SHIP_THRESHOLD = 699  # ₹ — free shipping above this (customer pays ₹0 shipping)
CUSTOMER_SHIP_CHARGE = 99  # ₹ — what customer pays if below threshold

# ─────────────────────────────────────────
# 2. CHANNEL AND CAMPAIGN CONFIG
# ─────────────────────────────────────────

CHANNELS = ["google_search", "meta", "email", "organic", "direct"]
CAMPAIGNS = {
    "CMP-GS-001": ("google", "Google Search — Brand + Darjeeling Intent",    "acquisition"),
    "CMP-GS-002": ("google", "Google Search — First Flush Seasonal",          "acquisition"),
    "CMP-GS-003": ("google", "Google Search — Chai + Daily Tea",              "acquisition"),
    "CMP-GS-004": ("google", "Google Search — Wellness + Green Tea",          "acquisition"),
    "CMP-GS-005": ("google", "Google Shopping — Product Catalog",             "acquisition"),
    "CMP-MT-001": ("meta",   "Meta Prospecting — Darjeeling Loyalist",        "acquisition"),
    "CMP-MT-002": ("meta",   "Meta Retargeting — Site Visitors",              "retargeting"),
    "CMP-MT-003": ("meta",   "Meta Prospecting — Gift + Festive",             "acquisition"),
    "CMP-EM-001": ("email",  "Email — Post-Purchase Day 7 Brewing Education", "retention"),
    "CMP-EM-002": ("email",  "Email — Day 21 Replenishment Nudge",            "retention"),
    "CMP-EM-003": ("email",  "Email — Day 45 Subscription Prompt",            "retention"),
    "CMP-EM-004": ("email",  "Email — First Flush Launch Announcement",       "retention"),
    "CMP-EM-005": ("email",  "Email — Winback 60+ Day Dormant",               "winback"),
    "CMP-EM-006": ("email",  "Email — Gift Buyer Self-Purchase Prompt",       "retention"),
}

CHANNEL_TO_CAMPAIGNS = {
    "google_search": ["CMP-GS-001", "CMP-GS-002", "CMP-GS-003", "CMP-GS-004", "CMP-GS-005"],
    "meta":          ["CMP-MT-001", "CMP-MT-002", "CMP-MT-003"],
    "email":         ["CMP-EM-001", "CMP-EM-002", "CMP-EM-003", "CMP-EM-004", "CMP-EM-005", "CMP-EM-006"],
    "organic":       [None],
    "direct":        [None],
}

INDIAN_CITIES = [
    "Mumbai", "Delhi", "Bengaluru", "Pune", "Chennai",
    "Kolkata", "Hyderabad", "Ahmedabad", "Jaipur", "Chandigarh",
    "Lucknow", "Kochi", "Indore", "Nagpur", "Surat",
]

# ─────────────────────────────────────────
# 3. SEASONAL WEIGHTS
# Weights control product mix probability by month.
# ─────────────────────────────────────────

# month -> {category: weight_multiplier}
SEASONAL_WEIGHTS = {
    1:  {"First Flush": 0.3, "Second Flush": 0.5, "Chai": 1.4, "Green Tea": 1.1, "Gift Box": 0.6},  # Jan
    2:  {"First Flush": 0.4, "Second Flush": 0.5, "Chai": 1.3, "Green Tea": 1.1, "Gift Box": 0.7},  # Feb
    3:  {"First Flush": 1.6, "Second Flush": 0.6, "Chai": 1.0, "Green Tea": 1.0, "Gift Box": 0.8},  # Mar — First Flush early
    4:  {"First Flush": 2.2, "Second Flush": 0.7, "Chai": 0.9, "Green Tea": 0.9, "Gift Box": 0.8},  # Apr — First Flush peak
    5:  {"First Flush": 1.2, "Second Flush": 1.4, "Chai": 0.9, "Green Tea": 0.9, "Gift Box": 0.8},  # May — Second Flush
    6:  {"First Flush": 0.5, "Second Flush": 1.8, "Chai": 1.0, "Green Tea": 1.0, "Gift Box": 0.7},  # Jun — Second Flush peak
    7:  {"First Flush": 0.3, "Second Flush": 1.0, "Chai": 1.1, "Green Tea": 1.2, "Gift Box": 0.6},  # Jul
    8:  {"First Flush": 0.3, "Second Flush": 0.8, "Chai": 1.2, "Green Tea": 1.2, "Gift Box": 0.7},  # Aug
    9:  {"First Flush": 0.3, "Second Flush": 0.7, "Chai": 1.3, "Green Tea": 1.0, "Gift Box": 1.0},  # Sep
    10: {"First Flush": 0.3, "Second Flush": 0.5, "Chai": 1.2, "Green Tea": 0.9, "Gift Box": 2.0},  # Oct — Diwali
    11: {"First Flush": 0.3, "Second Flush": 0.5, "Chai": 1.1, "Green Tea": 0.9, "Gift Box": 1.8},  # Nov — festive
    12: {"First Flush": 0.3, "Second Flush": 0.5, "Chai": 1.4, "Green Tea": 1.0, "Gift Box": 1.5},  # Dec — Christmas
}

# Monthly new customer volumes [SYNTHETIC]
MONTHLY_NEW_CUSTOMERS = {
    "2024-04": 16, "2024-05": 19, "2024-06": 18,
    "2024-07": 15, "2024-08": 14, "2024-09": 17,
    "2024-10": 28, "2024-11": 22, "2024-12": 24,
    "2025-01": 18, "2025-02": 17, "2025-03": 21,
    "2025-04": 32,  # First Flush 2025 spike
}

# ─────────────────────────────────────────
# 4. HELPER FUNCTIONS
# ─────────────────────────────────────────

def pick_product_for_month(month_num, customer_type, is_subscription=False, is_gift=False):
    if is_subscription:
        return random.choice(["SKU-011", "SKU-012"])
    if is_gift:
        return random.choice(["SKU-009", "SKU-010"])

    weights = SEASONAL_WEIGHTS.get(month_num, {})

    candidates = []
    base_weights_by_cat = {
        "First Flush": 12, "Second Flush": 10, "Chai": 20,
        "Green Tea": 10, "Pyramid Teabags": 12, "Cold Brew": 7, "Gift Box": 8,
    }

    for sku_id, p in PRODUCT_BY_ID.items():
        if p[3] in ["Subscription"]:  # skip subscription SKUs for regular orders
            continue
        if p[2] == "Gift Box" and not is_gift:  # gift box only via is_gift flag
            continue
        cat = p[2]
        base = base_weights_by_cat.get(cat, 5)
        mult = weights.get(cat, 1.0)
        # Returning customers skew toward premium and chai (they know what they like)
        if customer_type == "returning":
            if cat in ["First Flush", "Second Flush", "Chai"]:
                mult *= 1.4
        candidates.append((sku_id, base * mult))

    total = sum(w for _, w in candidates)
    r = random.uniform(0, total)
    cumulative = 0
    for sku_id, w in candidates:
        cumulative += w
        if r <= cumulative:
            return sku_id
    return candidates[-1][0]


def pick_discount(product_id, channel, is_new_customer):
    p = PRODUCT_BY_ID[product_id]
    cat = p[3]
    price = p[4]

    # Gift boxes: occasional seasonal discount
    if cat == "Gift Box" and random.random() < 0.20:
        pct = random.choice([0.10, 0.15])
        return round(price * pct, 2), f"DIWALI{int(pct*100)}"

    # New customer welcome discount via email/organic
    if is_new_customer and channel in ["email", "organic"] and random.random() < 0.25:
        return round(price * 0.10, 2), "WELCOME10"

    # Chai occasional replenishment discount
    if cat == "Chai" and channel == "email" and random.random() < 0.15:
        return round(price * 0.10, 2), "REPLEN10"

    return 0.0, "none"


def calc_order_economics(product_id, net_revenue, channel, campaign_id):
    p = PRODUCT_BY_ID[product_id]
    cogs = p[5]
    pkg = p[6]
    ship_cost = p[7]  # blended shipping cost Dorje bears
    gw_fee = round(net_revenue * GW_FEE_RATE, 2)

    # Shipping charged to customer
    if net_revenue >= FREE_SHIP_THRESHOLD:
        ship_charged = 0
    else:
        ship_charged = CUSTOMER_SHIP_CHARGE

    gross_margin = net_revenue - cogs - pkg - ship_cost - gw_fee
    gross_margin_pct = round(gross_margin / net_revenue * 100, 1) if net_revenue > 0 else 0

    # Attributed ad spend — paid channels carry spend; email/organic/direct carry near zero
    if channel == "google_search":
        attributed_spend = round(random.uniform(180, 420), 2)
    elif channel == "meta":
        attributed_spend = round(random.uniform(220, 500), 2)
    elif channel == "email":
        attributed_spend = round(random.uniform(5, 25), 2)  # email platform cost per send
    else:
        attributed_spend = 0.0

    contribution_margin = round(gross_margin - attributed_spend, 2)
    cm_pct = round(contribution_margin / net_revenue * 100, 1) if net_revenue > 0 else 0

    return {
        "ship_charged": ship_charged,
        "cogs": cogs,
        "pkg": pkg,
        "ship_cost": ship_cost,
        "gw_fee": gw_fee,
        "gross_margin": round(gross_margin, 2),
        "gross_margin_pct": gross_margin_pct,
        "attributed_spend": attributed_spend,
        "contribution_margin": contribution_margin,
        "cm_pct": cm_pct,
    }


# ─────────────────────────────────────────
# 5. GENERATE sample_orders.csv
# ─────────────────────────────────────────

def generate_orders():
    rows = []
    order_num = 1
    customer_pool = {}   # customer_id -> list of order dates (for returning logic)
    customer_counter = 1

    start_date = date(2024, 4, 1)
    end_date   = date(2025, 4, 30)

    current_date = start_date

    while current_date <= end_date:
        month_key = current_date.strftime("%Y-%m")
        month_num = current_date.month

        # How many orders on this day? Weekends slightly higher, festive months higher
        base_orders_per_day = MONTHLY_NEW_CUSTOMERS.get(month_key, 15) / 22
        if current_date.weekday() >= 5:  # weekend
            base_orders_per_day *= 1.3
        n_orders = max(0, int(random.gauss(base_orders_per_day * 1.6, 0.8)))

        for _ in range(n_orders):
            # Determine new vs returning
            if customer_pool and random.random() < 0.32:
                customer_type = "returning"
                customer_id = random.choice(list(customer_pool.keys()))
            else:
                customer_type = "new"
                customer_id = f"CUST-{customer_counter:04d}"
                customer_counter += 1
                customer_pool[customer_id] = []

            # Subscription order?
            is_subscription = (
                customer_type == "returning"
                and customer_id in customer_pool
                and len(customer_pool[customer_id]) >= 2
                and random.random() < 0.18
            )

            # Gift box order?
            is_gift = (
                not is_subscription
                and month_num in [10, 11, 12]
                and random.random() < 0.18
            ) or (
                not is_subscription
                and month_num not in [10, 11, 12]
                and random.random() < 0.06
            )

            product_id = pick_product_for_month(
                month_num, customer_type, is_subscription, is_gift
            )
            p = PRODUCT_BY_ID[product_id]
            price = p[4]
            category = p[2]   # p[2]=category, p[3]=pack_size_gm, p[4]=price

            # Channel
            if is_subscription or customer_type == "returning":
                channel = random.choices(
                    ["email", "direct", "organic", "google_search"],
                    weights=[45, 25, 20, 10]
                )[0]
            else:
                channel = random.choices(
                    ["google_search", "meta", "organic", "direct", "email"],
                    weights=[35, 15, 20, 18, 12]
                )[0]

            campaign_options = CHANNEL_TO_CAMPAIGNS[channel]
            campaign_id = random.choice(campaign_options) if campaign_options[0] else "none"

            discount_amt, discount_code = pick_discount(product_id, channel, customer_type == "new")
            gross_rev = price
            net_rev = round(gross_rev - discount_amt, 2)

            econ = calc_order_economics(product_id, net_rev, channel, campaign_id)

            week_str = f"{current_date.isocalendar()[0]}-W{current_date.isocalendar()[1]:02d}"

            rows.append({
                "order_id":           f"ORD-{current_date.year}-{order_num:04d}",
                "order_date":         current_date.strftime("%d/%m/%Y"),
                "week":               week_str,
                "month":              month_key,
                "customer_id":        customer_id,
                "customer_type":      customer_type,
                "product_id":         product_id,
                "product_name":       p[1],
                "product_category":   category,
                "quantity":           1,
                "gross_revenue":      gross_rev,
                "discount_amount":    discount_amt,
                "discount_code":      discount_code,
                "net_revenue":        net_rev,
                "shipping_charged":   econ["ship_charged"],
                "cogs":               econ["cogs"],
                "packaging_cost":     econ["pkg"],
                "shipping_cost":      econ["ship_cost"],
                "gateway_fee":        econ["gw_fee"],
                "gross_margin":       econ["gross_margin"],
                "gross_margin_pct":   econ["gross_margin_pct"],
                "attributed_ad_spend":econ["attributed_spend"],
                "contribution_margin":econ["contribution_margin"],
                "cm_pct":             econ["cm_pct"],
                "channel":            channel,
                "campaign_id":        campaign_id if campaign_id else "none",
                "city":               random.choice(INDIAN_CITIES),
                "is_subscription":    is_subscription,
                "is_gift":            is_gift,
            })

            customer_pool[customer_id].append(current_date)
            order_num += 1

        current_date += timedelta(days=1)

    # Write
    fields = list(rows[0].keys())
    with (SCRIPT_DIR / "sample_orders.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    print(f"sample_orders.csv: {len(rows)} rows written")
    return rows


# ─────────────────────────────────────────
# 6. GENERATE sample_ad_spend.csv
# ─────────────────────────────────────────

def generate_ad_spend():
    rows = []
    start_date = date(2024, 4, 1)
    end_date   = date(2025, 4, 30)

    # Weekly spend by campaign [SYNTHETIC]
    WEEKLY_SPEND = {
        "CMP-GS-001": 1800,  # Brand + Darjeeling Intent
        "CMP-GS-002": 1200,  # First Flush Seasonal (spikes in Mar-Apr)
        "CMP-GS-003": 900,   # Chai + Daily Tea
        "CMP-GS-004": 700,   # Wellness + Green Tea
        "CMP-GS-005": 600,   # Google Shopping
        "CMP-MT-001": 2200,  # Meta Prospecting — Loyalist
        "CMP-MT-002": 900,   # Meta Retargeting
        "CMP-MT-003": 1400,  # Meta — Gift + Festive (spikes Oct-Dec)
    }

    # Seasonal spend multipliers for paid campaigns
    SPEND_SEASONAL = {
        3: {"CMP-GS-002": 2.0, "CMP-MT-001": 1.4},  # First Flush ramp
        4: {"CMP-GS-002": 2.5, "CMP-MT-001": 1.6},  # First Flush peak
        5: {"CMP-GS-002": 1.3},
        10: {"CMP-MT-003": 2.2, "CMP-GS-001": 1.3}, # Diwali
        11: {"CMP-MT-003": 1.8, "CMP-GS-001": 1.2}, # Post-Diwali
        12: {"CMP-MT-003": 1.5, "CMP-GS-001": 1.1}, # Christmas
    }

    # Iterate weekly
    current = start_date
    while current <= end_date:
        week_end = current + timedelta(days=6)
        week_str = f"{current.isocalendar()[0]}-W{current.isocalendar()[1]:02d}"
        month_key = current.strftime("%Y-%m")
        month_num = current.month

        for cmp_id, base_spend in WEEKLY_SPEND.items():
            platform = CAMPAIGNS[cmp_id][0]
            name = CAMPAIGNS[cmp_id][1]
            objective = CAMPAIGNS[cmp_id][2]

            # Apply seasonal multiplier
            mult = SPEND_SEASONAL.get(month_num, {}).get(cmp_id, 1.0)
            spend = round(base_spend * mult * random.uniform(0.88, 1.12), 2)

            # Simulate impression/click/conversion metrics based on campaign type
            if platform == "google":
                cpm = round(random.uniform(180, 320), 2)
                ctr = round(random.uniform(3.8, 6.8), 2)
            else:  # meta
                cpm = round(random.uniform(220, 420), 2)
                ctr = round(random.uniform(1.2, 2.8), 2)

            impressions = int(spend / cpm * 1000)
            clicks = int(impressions * ctr / 100)
            cpc = round(spend / clicks, 2) if clicks > 0 else 0

            # Sessions: slight drop from clicks (some clicks don't fully load)
            sessions = int(clicks * random.uniform(0.87, 0.97))

            # Funnel rates
            atc_rate   = round(random.uniform(3.5, 7.5), 2)   # add to cart %
            co_rate    = round(random.uniform(50, 72), 2)      # checkout of ATC %
            cvr        = round(random.uniform(0.9, 3.8), 2)    # session to purchase %

            add_to_cart = int(sessions * atc_rate / 100)
            checkouts   = int(add_to_cart * co_rate / 100)
            orders_n    = max(0, int(sessions * cvr / 100))

            # Revenue estimate
            est_variable_cost_pct = random.uniform(0.38, 0.52)
            avg_order_value = random.uniform(520, 820)
            baseline_orders = max(1, int(sessions * cvr / 100))
            min_orders_for_plausible_cm = math.ceil(
                (spend * 0.31) / (avg_order_value * (1 - est_variable_cost_pct))
            )
            orders_n = max(baseline_orders, min_orders_for_plausible_cm)
            revenue = round(orders_n * avg_order_value, 2)

            new_customers = min(orders_n, max(1, int(orders_n * random.uniform(0.62, 0.88))))
            cac = round(spend / new_customers, 2) if new_customers > 0 else 0
            roas = round(revenue / spend, 2) if spend > 0 else 0

            # Contribution ROAS (after estimated variable costs ~45% of revenue)
            cm_revenue = revenue * (1 - est_variable_cost_pct)
            contribution_roas = round(cm_revenue / spend, 2) if spend > 0 else 0

            rows.append({
                "week":               week_str,
                "week_start":         current.strftime("%d/%m/%Y"),
                "week_end":           week_end.strftime("%d/%m/%Y"),
                "month":              month_key,
                "platform":           platform,
                "campaign_id":        cmp_id,
                "campaign_name":      name,
                "campaign_objective": objective,
                "spend":              spend,
                "impressions":        impressions,
                "clicks":             clicks,
                "ctr_pct":            ctr,
                "cpc":                cpc,
                "cpm":                cpm,
                "sessions":           sessions,
                "add_to_cart":        add_to_cart,
                "atc_rate_pct":       atc_rate,
                "checkouts":          checkouts,
                "checkout_rate_pct":  co_rate,
                "orders":             orders_n,
                "cvr_pct":            cvr,
                "revenue":            revenue,
                "new_customers":      new_customers,
                "cac":                cac,
                "roas":               roas,
                "contribution_roas":  contribution_roas,
                "status":             "active",
            })

        current += timedelta(weeks=1)

    fields = list(rows[0].keys())
    with (SCRIPT_DIR / "sample_ad_spend.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    print(f"sample_ad_spend.csv: {len(rows)} rows written")
    return rows


# ─────────────────────────────────────────
# 7. GENERATE sample_product_catalog.csv
# ─────────────────────────────────────────

def generate_product_catalog():
    rows = []
    for p in PRODUCTS:
        pid, name, cat, pack_gm, price, cogs, pkg, ship_blended, rung, segment, replen = p
        gw_fee_est = round(price * GW_FEE_RATE, 2)
        gross_margin_est = price - cogs - pkg - ship_blended - gw_fee_est
        gross_margin_pct = round(gross_margin_est / price * 100, 1)
        price_per_cup = round(price / (pack_gm / 2.5), 1)  # ~2.5g per cup

        rows.append({
            "product_id":           pid,
            "product_name":         name,
            "category":             cat,
            "pack_size_gm":         pack_gm,
            "price":                price,
            "cogs":                 cogs,
            "packaging_cost":       pkg,
            "shipping_cost_blended":ship_blended,
            "gateway_fee_est":      gw_fee_est,
            "gross_margin_est":     round(gross_margin_est, 2),
            "gross_margin_pct":     gross_margin_pct,
            "price_per_cup_est":    price_per_cup,
            "ladder_rung":          rung,
            "primary_segment":      segment,
            "replenishment_days":   replen,
            "is_subscription_sku":  "TRUE" if "Subscription" in cat else "FALSE",
            "is_gift_sku":          "TRUE" if cat == "Gift Box" else "FALSE",
            "data_label":           "[SYNTHETIC]",
        })

    fields = list(rows[0].keys())
    with (SCRIPT_DIR / "sample_product_catalog.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    print(f"sample_product_catalog.csv: {len(rows)} rows written")


# ─────────────────────────────────────────
# 8. GENERATE sample_customer_cohorts.csv
# ─────────────────────────────────────────

def generate_cohorts():
    """
    Monthly cohort table: M0 through M6 retention.
    Includes seasonal patterns — First Flush cohorts have higher LTV,
    festive (Oct-Nov) cohorts have higher M0 AOV but lower repeat rate.
    All values are [SYNTHETIC].
    """

    # Cohort parameters [SYNTHETIC]
    # (month_key, new_custs, m0_aov, m1_ret_rate, m2_ret_rate, m3_ret_rate,
    #  m4_ret_rate, m5_ret_rate, m6_ret_rate, sub_attach_m2, cac)
    COHORT_PARAMS = [
        ("2024-04", 16, 668, 0.22, 0.17, 0.14, 0.12, 0.10, 0.09, 0.08, 455),  # Apr — early First Flush
        ("2024-05", 19, 598, 0.19, 0.14, 0.11, 0.09, 0.08, 0.07, 0.07, 470),  # May
        ("2024-06", 18, 572, 0.18, 0.13, 0.10, 0.08, 0.07, 0.06, 0.07, 480),  # Jun
        ("2024-07", 15, 548, 0.16, 0.12, 0.09, 0.08, 0.07, 0.06, 0.06, 495),  # Jul
        ("2024-08", 14, 561, 0.17, 0.13, 0.10, 0.08, 0.07, 0.06, 0.07, 490),  # Aug
        ("2024-09", 17, 588, 0.19, 0.14, 0.11, 0.09, 0.08, 0.07, 0.08, 475),  # Sep
        ("2024-10", 28, 742, 0.25, 0.18, 0.14, 0.11, 0.09, 0.08, 0.10, 480),  # Oct — Diwali gifting spike (high M0 AOV, lower repeat)
        ("2024-11", 22, 648, 0.18, 0.13, 0.10, 0.08, 0.07, 0.06, 0.08, 510),  # Nov
        ("2024-12", 24, 712, 0.20, 0.16, 0.12, 0.10, 0.09, 0.08, 0.09, 490),  # Dec — Christmas gifting
        ("2025-01", 18, 538, 0.16, 0.12, 0.09, 0.08, 0.07, 0.06, 0.07, 520),  # Jan — post-festive dip
        ("2025-02", 17, 551, 0.17, 0.13, 0.10, 0.08, 0.07, 0.06, 0.07, 515),  # Feb
        ("2025-03", 21, 618, 0.22, 0.16, 0.13, 0.10, 0.09, 0.08, 0.09, 475),  # Mar — First Flush ramp
        ("2025-04", 32, 731, 0.28, 0.22, 0.17, 0.14, 0.12, 0.10, 0.13, 460),  # Apr — First Flush 2025 peak
    ]

    rows = []
    for params in COHORT_PARAMS:
        (month, new_custs, m0_aov,
         m1r, m2r, m3r, m4r, m5r, m6r,
         sub_attach, cac) = params

        m0_rev = round(new_custs * m0_aov * random.uniform(0.94, 1.06), 2)

        # Retained customers and revenue for each month
        def retained(rate):
            return max(1, round(new_custs * rate * random.uniform(0.88, 1.12)))

        def ret_rev(n, base_aov_mult=1.05):
            return round(n * m0_aov * base_aov_mult * random.uniform(0.9, 1.1), 2)

        m1_n = retained(m1r); m1_rev = ret_rev(m1_n)
        m2_n = min(m1_n, retained(m2r)); m2_rev = ret_rev(m2_n)
        m3_n = min(m2_n, retained(m3r)); m3_rev = ret_rev(m3_n, 1.08)
        m4_n = min(m3_n, retained(m4r)); m4_rev = ret_rev(m4_n, 1.10)
        m5_n = min(m4_n, retained(m5r)); m5_rev = ret_rev(m5_n, 1.10)
        m6_n = min(m5_n, retained(m6r)); m6_rev = ret_rev(m6_n, 1.12)

        cumulative_ltv = round(
            (m0_rev + m1_rev + m2_rev + m3_rev + m4_rev + m5_rev + m6_rev) / new_custs, 2
        )
        ltv_cac = round(cumulative_ltv / cac, 2)

        # Subscription: attach rate applied to M2+ returners
        sub_subscribers = max(0, round(m2_n * sub_attach))
        sub_monthly_rev = round(sub_subscribers * 649 * random.uniform(0.9, 1.1), 2)

        rows.append({
            "cohort_month":           month,
            "new_customers":          new_custs,
            "m0_orders":              new_custs,
            "m0_revenue":             m0_rev,
            "m0_avg_order_value":     m0_aov,
            "m1_retained":            m1_n,
            "m1_retention_rate_pct":  round(m1_n / new_custs * 100, 1),
            "m1_revenue":             m1_rev,
            "m2_retained":            m2_n,
            "m2_retention_rate_pct":  round(m2_n / new_custs * 100, 1),
            "m2_revenue":             m2_rev,
            "m3_retained":            m3_n,
            "m3_retention_rate_pct":  round(m3_n / new_custs * 100, 1),
            "m3_revenue":             m3_rev,
            "m4_retained":            m4_n,
            "m4_retention_rate_pct":  round(m4_n / new_custs * 100, 1),
            "m4_revenue":             m4_rev,
            "m5_retained":            m5_n,
            "m5_retention_rate_pct":  round(m5_n / new_custs * 100, 1),
            "m5_revenue":             m5_rev,
            "m6_retained":            m6_n,
            "m6_retention_rate_pct":  round(m6_n / new_custs * 100, 1),
            "m6_revenue":             m6_rev,
            "subscription_attach_m2_pct": round(sub_attach * 100, 1),
            "subscription_subscribers_m2": sub_subscribers,
            "subscription_monthly_rev":    sub_monthly_rev,
            "cumulative_ltv_m6":      cumulative_ltv,
            "cac_cohort":             cac,
            "ltv_cac_ratio_m6":       ltv_cac,
            "data_label":             "[SYNTHETIC]",
        })

    fields = list(rows[0].keys())
    with (SCRIPT_DIR / "sample_customer_cohorts.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    print(f"sample_customer_cohorts.csv: {len(rows)} rows written")


# ─────────────────────────────────────────
# 9. RUN
# ─────────────────────────────────────────

if __name__ == "__main__":
    print("Generating Dorje Teas synthetic datasets...")
    print("All values are [SYNTHETIC]. No internal Dorje data used.\n")
    generate_orders()
    generate_ad_spend()
    generate_product_catalog()
    generate_cohorts()
    print(f"\nDone. All CSVs written to {SCRIPT_DIR}.")
    print("Replace [SYNTHETIC] files only when authorized internal Shopify/Ads exports are available.")
