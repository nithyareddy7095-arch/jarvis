import 'package:flutter/material.dart';

import '../services/api_service.dart';
import '../widgets/bhoomi_avatar.dart';

class BhoomiChatScreen extends StatefulWidget {
  const BhoomiChatScreen({super.key});

  @override
  State<BhoomiChatScreen> createState() => _BhoomiChatScreenState();
}

class _BhoomiChatScreenState extends State<BhoomiChatScreen> {
  final _api = ApiService();
  final _controller = TextEditingController();
  String _reply = 'Ask Bhoomi anything about farming.';

  Future<void> _ask() async {
    final res = await _api.askBhoomi(_controller.text.trim());
    setState(() => _reply = '${res.answer}\n\nTips: ${res.tips.join(' | ')}');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Bhoomi AI Assistant')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            const BhoomiAvatar(state: 'talking'),
            TextField(controller: _controller, decoration: const InputDecoration(labelText: 'Type question')),
            const SizedBox(height: 10),
            ElevatedButton(onPressed: _ask, child: const Text('Ask Bhoomi')),
            const SizedBox(height: 16),
            Expanded(child: SingleChildScrollView(child: Text(_reply))),
          ],
        ),
      ),
    );
  }
}
