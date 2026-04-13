import 'package:flutter/material.dart';

import '../services/api_service.dart';

class WeatherScreen extends StatefulWidget {
  const WeatherScreen({super.key});

  @override
  State<WeatherScreen> createState() => _WeatherScreenState();
}

class _WeatherScreenState extends State<WeatherScreen> {
  final _api = ApiService();
  Map<String, dynamic>? _weather;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final data = await _api.weather(17.385, 78.4867);
    setState(() => _weather = data);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Weather Advisory')),
      body: _weather == null
          ? const Center(child: CircularProgressIndicator())
          : ListView(
              padding: const EdgeInsets.all(16),
              children: [
                ListTile(title: const Text('Temperature'), subtitle: Text('${_weather!['temperature_c']} °C')),
                ListTile(title: const Text('Humidity'), subtitle: Text('${_weather!['humidity']} %')),
                ListTile(title: const Text('Rainfall'), subtitle: Text('${_weather!['rainfall_mm']} mm')),
                ListTile(title: const Text('Irrigation Advisory'), subtitle: Text(_weather!['advisory'] ?? '')),
              ],
            ),
    );
  }
}
