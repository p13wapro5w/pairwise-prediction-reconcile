"""第 58 批：200ms 延迟下松开摇杆，角色还会往前滑半米，服务器校正时直接..."""

def tick_rate(client_hz, server_hz):
    """返回客户端与服务器 tick 比。"""
    raise NotImplementedError("TODO: tick_rate")

def replay_count(inputs, lost):
    """返回重放输入数量。"""
    raise NotImplementedError("TODO: replay_count")

def rollback_state(state, snapshot):
    """回滚到快照。"""
    raise NotImplementedError("TODO: rollback_state")

def lag_compensation(rtt, max_comp):
    """返回延迟补偿上限。"""
    raise NotImplementedError("TODO: lag_compensation")

def bind_vehicle(player_pos, vehicle_pos):
    """绑定角色与载具状态。"""
    raise NotImplementedError("TODO: bind_vehicle")

def predict_collision(next_pos, wall):
    """预测碰撞。"""
    raise NotImplementedError("TODO: predict_collision")

def clock_offset(server_time, client_time):
    """返回时钟偏移。"""
    raise NotImplementedError("TODO: clock_offset")

def dedupe_inputs(seqs):
    """按序号去重。"""
    raise NotImplementedError("TODO: dedupe_inputs")

def correct_threshold(drift, base):
    """返回自适应校正阈值。"""
    raise NotImplementedError("TODO: correct_threshold")

def snapshot_key(tick, version):
    """返回快照键。"""
    raise NotImplementedError("TODO: snapshot_key")
