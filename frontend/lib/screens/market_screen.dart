import 'package:flutter/material.dart';

import '../models/models.dart';
import '../services/api_service.dart';

class MarketScreen extends StatefulWidget {
  const MarketScreen({super.key});

  @override
  State<MarketScreen> createState() => _MarketScreenState();
}

class _MarketScreenState extends State<MarketScreen> {
  final _api = ApiService();
  List<MarketPrice> _prices = [];

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final data = await _api.marketPrices('tomato');
    setState(() => _prices = data);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Market Price Intelligence')),
      body: ListView.builder(
        itemCount: _prices.length,
        itemBuilder: (_, i) {
          final p = _prices[i];
          return Card(
            child: ListTile(
              title: Text('${p.crop} @ ${p.market}'),
              subtitle: Text('Conventional: ₹${p.conventionalPrice} | Organic: ₹${p.organicPrice}\nTrend: ${p.demandTrend}'),
            ),
          );
        },
      ),
    );
  }
}
