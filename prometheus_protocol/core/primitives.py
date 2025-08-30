from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class UserIdentity(BaseModel):
    """
    Represents a sovereign user, referencing their decentralized ID from EmPower1.
    """
    did: UUID = Field(default_factory=uuid4, description="The user's unique Decentralized Identifier.")
    name: str = Field(..., description="The user's chosen name or alias.")

class NodeType(str, Enum):
    """
    Enumeration for the different types of nodes in the network.
    """
    SENTINEL = "sentinel"
    NOMAD = "nomad"
    ECHO = "echo"

class NetworkNode(BaseModel):
    """
    An abstract representation of a participant in a network.
    """
    node_id: UUID = Field(default_factory=uuid4, description="The unique identifier for the network node.")
    node_type: NodeType = Field(..., description="The type of the node (e.g., Sentinel, Nomad).")

class DataStream(BaseModel):
    """
    Represents a flow of information, such as an audio feed or data packet.
    """
    stream_id: UUID = Field(default_factory=uuid4, description="The unique identifier for the data stream.")
    source_node: UUID = Field(..., description="The ID of the node where the stream originates.")
    destination_node: UUID = Field(..., description="The ID of the node where the stream terminates.")

class SmartContract(BaseModel):
    """
    The logical, executable core of a decentralized application (dApp).
    """
    contract_address: str = Field(..., description="The on-chain address of the smart contract.")
    abi: dict = Field(..., description="The Application Binary Interface (ABI) of the contract.")

class DigitalAsset(BaseModel):
    """
    A representation of a unique, ownable digital item, managed by EmPower1.
    """
    asset_id: UUID = Field(default_factory=uuid4, description="The unique identifier for the digital asset.")
    owner_did: UUID = Field(..., description="The Decentralized Identifier of the user who owns the asset.")
    metadata: dict = Field(default_factory=dict, description="A dictionary containing metadata about the asset.")
