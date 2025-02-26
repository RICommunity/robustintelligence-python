# coding: utf-8

"""
    Robust Intelligence REST API

    API methods for Robust Intelligence. Users must authenticate using the `rime-api-key` header.

    The version of the OpenAPI document: 1.0
    Contact: dev@robustintelligence.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class JobStatus(str, Enum):
    """
    Status of the RimeJob.   - JOB_STATUS_PENDING: Resources have been created for the job but the job has not started yet.  - JOB_STATUS_FAILED: Blanket status for user or system-related job failure.  - JOB_STATUS_REQUESTED: The job descriptor exists but has no resources allocated. Jobs that remain in this status without moving to the PENDING status are at risk of entering the FAILED status.  - JOB_STATUS_CANCELLED: Job has been cancelled. Cancelled jobs cannot be recovered.
    """

    """
    allowed enum values
    """
    JOB_STATUS_PENDING = 'JOB_STATUS_PENDING'
    JOB_STATUS_RUNNING = 'JOB_STATUS_RUNNING'
    JOB_STATUS_FAILED = 'JOB_STATUS_FAILED'
    JOB_STATUS_SUCCEEDED = 'JOB_STATUS_SUCCEEDED'
    JOB_STATUS_REQUESTED = 'JOB_STATUS_REQUESTED'
    JOB_STATUS_CANCELLED = 'JOB_STATUS_CANCELLED'
    JOB_STATUS_UNSPECIFIED = 'JOB_STATUS_UNSPECIFIED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobStatus from a JSON string"""
        return cls(json.loads(json_str))


