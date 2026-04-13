import 'package:flutter/material.dart';

import '../widgets/bhoomi_avatar.dart';

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final cards = [
      ('Bhoomi Chat', '/chat', Icons.smart_toy),
      ('Disease Scanner', '/scanner', Icons.camera_alt),
      ('Weather', '/weather', Icons.cloud),
      ('Market Prices', '/market', Icons.currency_rupee),
      ('Farm Learning', '/learning', Icons.travel_explore),
      ('Community', '/community', Icons.groups),
      ('Profile', '/profile', Icons.person),
    ];

    return Scaffold(
      appBar: AppBar(title: const Text('Farmer Dashboard')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            const Align(alignment: Alignment.centerRight, child: BhoomiAvatar(state: 'idle')),
            const SizedBox(height: 12),
            Expanded(
              child: GridView.count(
                crossAxisCount: 2,
                childAspectRatio: 1.4,
                children: cards
                    .map(
                      (c) => Card(
                        child: InkWell(
                          onTap: () => Navigator.pushNamed(context, c.$2),
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [Icon(c.$3 as IconData), const SizedBox(height: 8), Text(c.$1 as String)],
                          ),
                        ),
                      ),
                    )
                    .toList(),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
