import 'package:flutter/material.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Farmer Profile')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: const [
          CircleAvatar(radius: 38, child: Icon(Icons.person, size: 42)),
          SizedBox(height: 16),
          ListTile(title: Text('Name'), subtitle: Text('Farmer Asha')),
          ListTile(title: Text('Farm'), subtitle: Text('Asha Green Farm')),
          ListTile(title: Text('Crop Types'), subtitle: Text('Tomato, Chilli, Millets')),
          ListTile(title: Text('Soil Type'), subtitle: Text('Sandy Loam')),
          ListTile(title: Text('GPS Location'), subtitle: Text('17.385, 78.4867')),
          ListTile(title: Text('Bhoomi Growth Stage'), subtitle: Text('Stage 2 - Plant')),
        ],
      ),
    );
  }
}
