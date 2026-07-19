import numpy as np

from itif.generate import GeneratorConfig, generate_events
from itif.model import assign_actions, fit_hybrid, score_exclusion, score_hybrid


def test_generator_is_reproducible():
    cfg = GeneratorConfig(seed=7, n_events=500, n_identities=300, n_devices=80, n_issuers=8)
    a = generate_events(cfg)
    b = generate_events(cfg)
    assert a.equals(b)
    assert {"fraud", "novel_fraud", "exclusion"}.issubset(a.columns)


def test_hybrid_scores_and_actions_are_valid():
    df = generate_events(GeneratorConfig(seed=9, n_events=1200, n_identities=650, n_devices=180, n_issuers=12))
    train, test = df.iloc[:900], df.iloc[900:]
    model = fit_hybrid(train, (0.5, 0.25, 0.25), seed=9)
    scored = score_hybrid(model, test)
    exclusion = score_exclusion(train, test)
    actions = assign_actions(scored.risk.to_numpy(), {"monitor": .35, "step_up": .55, "human_review": .72, "block": .9})
    assert np.isfinite(scored.to_numpy()).all()
    assert ((scored >= 0) & (scored <= 1)).all().all()
    assert ((exclusion >= 0) & (exclusion <= 1)).all()
    assert set(actions) <= {"approve", "monitor", "step_up", "human_review", "block_or_escalate"}

