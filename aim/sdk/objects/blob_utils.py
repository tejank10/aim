import os
import uuid
import datetime

from aim.storage.utils import BLOB, ExtBLOB

USE_EXT_BLOBS = os.environ.get('__AIM_USE_EXTERNAL_BLOBS__')


def _make_ext_blob(data: object, object_class: str = 'object'):
    now_ = datetime.datetime.utcnow().strftime('%Y.%m.%d-%H:%M')
    hash_ = uuid.uuid4().hex[:16]
    ext_path = f'{object_class}/{now_}/{hash_}-{object_class}'
    return ExtBLOB(data=data, ext_path=ext_path)


def _make_blob(data: object, object_class: str = 'object'):
    return BLOB(data=data)


create_blob = _make_ext_blob if USE_EXT_BLOBS else _make_blob
