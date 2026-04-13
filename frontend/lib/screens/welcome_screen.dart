import 'package:flutter/material.dart';

class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.eco, size: 72, color: Colors.green),
            const SizedBox(height: 12),
            const Text('Travel with Farmer', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
            const Text('Sustainable farming with Bhoomi AI'),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => Navigator.pushNamed(context, '/auth'),
              child: const Text('Get Started'),
            )
          ],
        ),
      ),
    );
  }
}
