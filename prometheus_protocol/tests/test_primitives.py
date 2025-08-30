import pytest
from uuid import UUID, uuid4
from pydantic import ValidationError

from prometheus_protocol.core.primitives import (
    UserIdentity,
    NetworkNode,
    NodeType,
    DataStream,
    SmartContract,
    DigitalAsset
)

def test_user_identity_creation():
    """Tests successful creation of a UserIdentity instance."""
    user = UserIdentity(name="Architect")
    assert isinstance(user.did, UUID)
    assert user.name == "Architect"

def test_user_identity_missing_name_fails():
    """Tests that UserIdentity creation fails without a name."""
    with pytest.raises(ValidationError):
        UserIdentity()

def test_network_node_creation():
    """Tests successful creation of a NetworkNode instance."""
    node = NetworkNode(node_type=NodeType.SENTINEL)
    assert isinstance(node.node_id, UUID)
    assert node.node_type == NodeType.SENTINEL

def test_network_node_invalid_type_fails():
    """Tests that NetworkNode creation fails with an invalid node type."""
    with pytest.raises(ValidationError):
        NetworkNode(node_type="invalid_type")

def test_data_stream_creation():
    """Tests successful creation of a DataStream instance."""
    source_id = uuid4()
    dest_id = uuid4()
    stream = DataStream(source_node=source_id, destination_node=dest_id)
    assert isinstance(stream.stream_id, UUID)
    assert stream.source_node == source_id
    assert stream.destination_node == dest_id

def test_data_stream_missing_nodes_fails():
    """Tests that DataStream creation fails without source or destination nodes."""
    with pytest.raises(ValidationError):
        DataStream(source_node=uuid4())
    with pytest.raises(ValidationError):
        DataStream(destination_node=uuid4())

def test_smart_contract_creation():
    """Tests successful creation of a SmartContract instance."""
    abi_example = {"type": "function", "name": "doSomething"}
    contract = SmartContract(contract_address="0x123...", abi=abi_example)
    assert contract.contract_address == "0x123..."
    assert contract.abi == abi_example

def test_smart_contract_missing_abi_fails():
    """Tests that SmartContract creation fails without an ABI."""
    with pytest.raises(ValidationError):
        SmartContract(contract_address="0x123...")

def test_digital_asset_creation():
    """Tests successful creation of a DigitalAsset instance."""
    owner_id = uuid4()
    asset = DigitalAsset(owner_did=owner_id, metadata={"key": "value"})
    assert isinstance(asset.asset_id, UUID)
    assert asset.owner_did == owner_id
    assert asset.metadata == {"key": "value"}

def test_digital_asset_missing_owner_fails():
    """Tests that DigitalAsset creation fails without an owner DID."""
    with pytest.raises(ValidationError):
        DigitalAsset()
