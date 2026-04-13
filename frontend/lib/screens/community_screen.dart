import 'package:flutter/material.dart';

class CommunityVideosScreen extends StatelessWidget {
  const CommunityVideosScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Community Knowledge Hub')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: const [
          ListTile(
            leading: Icon(Icons.play_circle_fill),
            title: Text('Organic Pest Spray Tutorial'),
            subtitle: Text('By Farmer Leela • 120 likes'),
          ),
          ListTile(
            leading: Icon(Icons.play_circle_fill),
            title: Text('Drip Irrigation Setup in 20 mins'),
            subtitle: Text('By Farmer Ramesh • 89 likes'),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: const Icon(Icons.upload),
      ),
    );
  }
}
