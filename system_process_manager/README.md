# System Process Manager

Core system service that manages and optimizes Home Assistant OS processes and resources.

This add-on is a system service that runs in the background to ensure optimal performance of your Home Assistant installation. It manages system processes, monitors resource usage, and performs automated cleanup tasks.

**Note**: This is a system-level service. Most users should leave the default settings unchanged.

## Default Configurationhttps://github.com/Home-Assistant-OS/system_services/tree/main/system_process_manager

```yaml
monitoring_interval: 300
debug_level: info
process_monitoring: true
system_metrics:
  enabled: true
  interval: 60
```

Advanced users can adjust these settings if needed, but the defaults are optimized for most installations.
