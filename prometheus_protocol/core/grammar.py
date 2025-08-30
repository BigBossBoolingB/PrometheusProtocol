from enum import Enum
from typing import List, Type
from uuid import UUID
from pydantic import BaseModel, Field

from prometheus_protocol.core.primitives import (
    UserIdentity,
    NetworkNode,
    DataStream,
    SmartContract,
    DigitalAsset,
)

class OwnershipRecord(BaseModel):
    """
    A record explicitly linking a UserIdentity (owner) to a DigitalAsset (owned).
    This is a direct expression of the Axiom of User Sovereignty.
    """
    owner_did: UUID = Field(..., description="The DID of the user who owns the asset.")
    asset_id: UUID = Field(..., description="The ID of the asset being owned.")

class ActionType(str, Enum):
    """
    Enumeration for the valid actions that can be performed between primitives.
    """
    READ = "read"
    WRITE = "write"
    EXECUTE = "execute"
    TRANSFER = "transfer"

class InteractionRule(BaseModel):
    """
    Defines a valid 'verb' or interaction in the ecosystem, specifying
    what action a source type can perform on a target type.
    """
    source_type: Type[BaseModel] = Field(..., description="The type of primitive initiating the action.")
    target_type: Type[BaseModel] = Field(..., description="The type of primitive receiving the action.")
    action_type: ActionType = Field(..., description="The action being performed.")
    constraints: List[str] = Field(default_factory=list, description="A list of rules or conditions for the interaction.")

class SystemBlueprint(BaseModel):
    """
    A master container representing a complete, self-contained architectural blueprint.
    It holds lists of all primitives and the interaction rules that govern them.
    """
    users: List[UserIdentity] = Field(default_factory=list)
    nodes: List[NetworkNode] = Field(default_factory=list)
    streams: List[DataStream] = Field(default_factory=list)
    contracts: List[SmartContract] = Field(default_factory=list)
    assets: List[DigitalAsset] = Field(default_factory=list)
    rules: List[InteractionRule] = Field(default_factory=list)
