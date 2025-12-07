import json

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import InfoBar, InfoBarIcon, InfoBarPosition

from core.config.config_set import ConfigSet
from gui.util.translator import baasTranslator as bt


def success(label: str, msg: str, config: ConfigSet, duration: int = 800) -> None:
    config.get_signal('notify_signal').emit(json.dumps({
        'type': 'success',
        'label': label,
        'msg': msg,
        'duration': duration
    }))


def error(label: str, msg: str, config: ConfigSet, duration: int = 800) -> None:
    config.get_signal('notify_signal').emit(json.dumps({
        'type': 'error',
        'label': label,
        'msg': msg,
        'duration': duration
    }))


def warning(label: str, msg: str, config: ConfigSet, duration: int = 800) -> None:
    config.get_signal('notify_signal').emit(json.dumps({
        'type': 'warning',
        'label': label,
        'msg': msg,
        'duration': duration
    }))


def _success(label: str, msg: str, info_widget: QWidget, duration: int = 800, customized=False) -> None:
    success_suffix = "" if customized else bt.tr('ConfigTranslation', '设置成功')
    InfoBar(
        icon=InfoBarIcon.SUCCESS,
        title=f'{label}{success_suffix}',
        content=f'{msg}',
        orient=Qt.Vertical,
        position=InfoBarPosition.BOTTOM_RIGHT,
        duration=duration,
        parent=info_widget
    ).show()


def _error(label: str, msg: str, info_widget: QWidget, duration: int = 800, customized=False) -> None:
    error_suffix = "" if customized else bt.tr('ConfigTranslation', '设置失败')
    InfoBar(
        icon=InfoBarIcon.ERROR,
        title=f'{label}{error_suffix}',
        content=f'{msg}',
        orient=Qt.Vertical,
        position=InfoBarPosition.BOTTOM_RIGHT,
        duration=duration,
        parent=info_widget
    ).show()


def _warning(label: str, settled: str, info_widget: QWidget, duration: int = 800) -> None:
    warning_title = bt.tr('ConfigTranslation', '警告')
    warning_content = bt.tr('ConfigTranslation', '设置可能会出现问题，当前值为：')
    InfoBar(
        icon=InfoBarIcon.WARNING,
        title=warning_title,
        content=f'{label}{warning_content}{settled}',
        orient=Qt.Vertical,
        position=InfoBarPosition.BOTTOM_RIGHT,
        duration=duration,
        parent=info_widget
    ).show()
