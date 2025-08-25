# models.py

# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union

# --- 基底模型 ---
class BaseComponentModel(BaseModel):
    component_id: str
    model_name: str
    type: str
    manufacturer: str
    weight_g: Optional[float] = None
    dimensions_mm: Optional[Union[List[float], Dict[str, Any]]] = None
    datasheet_url: Optional[str] = None
    notes: Optional[str] = None
    status: str
    suggested_retail_price_usd: Optional[float] = None
    suppliers: List[str]
    mtbf_hours: Optional[int] = None
    after_sales_support: str
    maintenance_cycle_recommendations: str
    environmental_adaptability: Dict[str, Any]
    keywords: List[str]

# --- 子模型 ---
class MotorModel(BaseComponentModel):
    application_type: str
    kv_value: int
    max_current_a: int
    rated_power_w: int
    voltage_range_v: List[float]

class PropellerModel(BaseComponentModel):
    application_type: str
    diameter_inch: float
    pitch_inch: float
    material: str
    blade_count: int

class ESCModel(BaseComponentModel):
    application_type: str
    rated_current_a: int
    burst_current_a: int
    input_voltage_v: List[float]
    firmware_protocol: str

class BatteryModel(BaseComponentModel):
    application_type: str
    capacity_mah: int
    nominal_voltage_v: float
    discharge_rate_c: int
    cell_count_s: int
    energy_density_wh_per_kg: float

class IMUModel(BaseComponentModel):
    included_sensors: List[str]
    update_frequency_hz: int
    interface_type: str

class CameraModel(BaseComponentModel):
    sensor_type: str
    resolution: List[int]
    frame_rate_fps: int
    video_output_format: str

class FrameDimensions(BaseModel):
    wheelbase_mm: int
    wingspan_mm: int
    length_width_height_mm: List[float]

class FrameModel(BaseComponentModel):
    drone_type: str
    configuration: str
    material: str
    dimensions: FrameDimensions
    max_takeoff_weight_capacity_kg: float

class LandingGearModel(BaseComponentModel):
    max_load_capacity_kg: float
    retraction_mechanism: str

class EnclosureModel(BaseComponentModel):
    ip_rating: str
    material: str

class GNSSModel(BaseComponentModel):
    supported_satellite_systems: List[str]
    update_frequency_hz: int
    
class FirmwareModel(BaseModel):
    software_id: str
    model_name: str = Field(alias='name')
    latest_version: str
    supported_drone_types: List[str]
    license_model: str
    keywords: List[str]
    notes: Optional[str] = None
    
class WirelessModel(BaseComponentModel):
    communication_standard: str
    frequency_band: str
    max_data_rate_mbps: Union[float, int]

# --- 外層容器模型 ---
class PowerModule(BaseModel):
    motors: List[MotorModel] = Field(default_factory=list)
    propellers: List[PropellerModel] = Field(default_factory=list)
    escs: List[ESCModel] = Field(default_factory=list)
    batteries: List[BatteryModel] = Field(default_factory=list)

class SensorModule(BaseModel):
    inertial_measurement_units: List[IMUModel] = Field(default_factory=list)
    gnss_receivers: List[GNSSModel] = Field(default_factory=list)
    cameras: List[CameraModel] = Field(default_factory=list)
    flight_controller_firmware_software: List[FirmwareModel] = Field(default_factory=list)
    wireless_communication_modules: List[WirelessModel] = Field(default_factory=list)

class StructureModule(BaseModel):
    frames_chassis: List[FrameModel] = Field(default_factory=list)
    landing_gears: List[LandingGearModel] = Field(default_factory=list)
    enclosures_covers: List[EnclosureModel] = Field(default_factory=list)

class DroneKnowledgeBase(BaseModel):
    drone_propulsion_and_energy_modules: Optional[PowerModule] = None
    drone_sensing_and_datalink_modules: Optional[SensorModule] = None
    drone_structure_and_airframe_modules: Optional[StructureModule] = None

    class Config:
        extra = 'ignore'
