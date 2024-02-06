import random as rd

## Independent Variables (i.e. configurable)

# V_max
open_interest_cap = rd.randint(1, 100)

# λ_max
maximum_initial_leverage = rd.randint(1, 100)

# skew_scale
skew_scaling_denominator_constant = rd.randint(1, 100)

# ϕt
taker_fee = rd.randint(1, 100)

# ϕm
maker_fee = rd.randint(1, 100)

# W_max
max_funding_skew_threshold = rd.randint(1, 100)

# i_max
max_funding_rate = rd.randint(1, 100)

# r_buffer
liquidation_buffer_ratio = rd.randint(1, 100)

# r_fee
liquidation_fee_ratio = rd.randint(1, 100)

# D (this is a reused variable)
minimal_keeper_incentive = rd.randint(1, 100)

## Dependent Variables (i.e. calculated)

# b
base_asset = rd.randint(1, 100)

# p
base_asset_spot_price = rd.randint(1, 100)

# p_e
initial_base_asset_spot_price = rd.randint(1, 100)

# q
position_size = rd.randint(1, 100)

# p_d
position_debt = rd.randint(1, 100)

# v
notional_value = rd.randint(1, 100)

# v_e
initial_notional_value = rd.randint(1, 100)

# r
profit_and_loss = rd.randint(1, 100)

# C
set_of_all_positions_in_the_market = []

# C_long
set_of_all_long_positions_in_the_market = []

# C_short
set_of_all_short_positions_in_the_market = []

# Q
market_size = rd.randint(1, 100)

# K
market_skew = rd.randint(1, 100)

# λ
leverage = rd.randint(1, 100)

# λ_e
initial_leverage = rd.randint(1, 100)

# m_e
initial_margin = rd.randint(1, 100)

# m
remaining_margin = rd.randint(1, 100)

# W
proportional_skew = rd.randint(1, 100)

# i
instantaneous_funding_rate = rd.randint(1, 100)

# t_last
skew_last_modified = rd.randint(1, 100)

# F
cumulative_funding_sequence = rd.randint(1, 100)

# u
unrecorded_base_funding = rd.randint(1, 100)

# F_now
unrecorded_cumulative_funding = rd.randint(1, 100)

# F_j
unrecorded_cumulative_funding_at_last_modified_index = rd.randint(1, 100)

# j
last_modified_index = rd.randint(1, 100)

# f
accrued_position_funding = rd.randint(1, 100)

# Δe
aggregate_position_entry_debt_correction = rd.randint(1, 100)

# D (this is a reused variable)
market_debt = rd.randint(1, 100)

# liq_margin
liquidation_margin = rd.randint(1, 100)

# p_liq_approx
approximate_liquidation_price = rd.randint(1, 100)
