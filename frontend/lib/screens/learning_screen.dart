import 'package:flutter/material.dart';

class LearningMarketplaceScreen extends StatelessWidget {
  const LearningMarketplaceScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final farms = [
      ('Sunrise Organic Farm', 'Hydroponics Tour', '₹499'),
      ('Millet Trails', 'Hybrid Farming Workshop', '₹699'),
      ('Green Roots Estate', 'Soil Health Masterclass', '₹399'),
    ];

    return Scaffold(
      appBar: AppBar(title: const Text('Travel with Farmer Marketplace')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: farms
            .map((f) => Card(
                  child: ListTile(
                    title: Text(f.$1),
                    subtitle: Text(f.$2),
                    trailing: ElevatedButton(onPressed: () {}, child: Text(f.$3)),
                  ),
                ))
            .toList(),
      ),
    );
  }
}
