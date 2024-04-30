import os
import pytest


@pytest.fixture
def folders(tmp_path):
    in_folder = os.path.join(tmp_path, "In")
    ok_folder = os.path.join(tmp_path, "Ok")
    err_folder = os.path.join(tmp_path, "Err")
    out_folder = os.path.join(tmp_path, "Out")
    os.makedirs(in_folder, exist_ok=True)
    os.makedirs(ok_folder, exist_ok=True)
    os.makedirs(err_folder, exist_ok=True)
    os.makedirs(out_folder, exist_ok=True)
    return {
        "in_folder": in_folder,
        "out_folder": out_folder,
        "ok_folder": ok_folder,
        "err_folder": err_folder,
    }
