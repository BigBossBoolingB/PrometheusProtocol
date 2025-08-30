import pytest
from uuid import uuid4
from pydantic import ValidationError

from prometheus_protocol.core.primitives import (
    UserIdentity,
    DigitalAsset,
    DataStream
)
from prometheus_protocol.core.grammar import (
    OwnershipRecord,
    ActionType,
    InteractionRule,
    SystemBlueprint
)

def test_ownership_record_creation():
    """Tests successful creation of an OwnershipRecord."""
    owner_id = uuid4()
    asset_id = uuid4()
    record = OwnershipRecord(owner_did=owner_id, asset_id=asset_id)
    assert record.owner_did == owner_id
    assert record.asset_id == asset_id

def test_ownership_record_missing_fields_fails():
    """Tests that OwnershipRecord creation fails if fields are missing."""
    with pytest.raises(ValidationError):
        OwnershipRecord(owner_did=uuid4())
    with pytest.raises(ValidationError):
        OwnershipRecord(asset_id=uuid4())

def test_interaction_rule_creation():
    """Tests successful creation of an InteractionRule."""
    rule = InteractionRule(
        source_type=UserIdentity,
        target_type=DataStream,
        action_type=ActionType.READ,
        constraints=["user.is_active"]
    )
    assert rule.source_type == UserIdentity
    assert rule.target_type == DataStream
    assert rule.action_type == ActionType.READ
    assert rule.constraints == ["user.is_active"]

def test_interaction_rule_invalid_action_fails():
    """Tests that InteractionRule creation fails with an invalid action type."""
    with pytest.raises(ValidationError):
        InteractionRule(
            source_type=UserIdentity,
            target_type=DataStream,
            action_type="some_invalid_action"
        )

def test_system_blueprint_empty_creation():
    """Tests that an empty SystemBlueprint can be created successfully."""
    blueprint = SystemBlueprint()
    assert blueprint.users == []
    assert blueprint.nodes == []
    assert blueprint.streams == []
    assert blueprint.contracts == []
    assert blueprint.assets == []
    assert blueprint.rules == []

def test_system_blueprint_populated_creation():
    """Tests creation of a SystemBlueprint with populated data."""
    user = UserIdentity(name="Test User")
    asset = DigitalAsset(owner_did=user.did)
    rule = InteractionRule(
        source_type=UserIdentity,
        target_type=DigitalAsset,
        action_type=ActionType.TRANSFER
    )

    blueprint = SystemBlueprint(
        users=[user],
        assets=[asset],
        rules=[rule]
    )

    assert len(blueprint.users) == 1
    assert blueprint.users[0].name == "Test User"
    assert len(blueprint.assets) == 1
    assert blueprint.assets[0].owner_did == user.did
    assert len(blueprint.rules) == 1
    assert blueprint.rules[0].action_type == ActionType.TRANSFER
