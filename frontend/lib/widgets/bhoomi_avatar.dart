import 'package:flutter/material.dart';
import 'package:rive/rive.dart';

class BhoomiAvatar extends StatelessWidget {
  final String state;
  const BhoomiAvatar({super.key, required this.state});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(8),
      decoration: BoxDecoration(
        color: Colors.green.shade50,
        borderRadius: BorderRadius.circular(16),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          SizedBox(
            height: 120,
            width: 120,
            child: RiveAnimation.asset(
              'assets/rive/bhoomi.riv',
              fit: BoxFit.contain,
              animations: [state],
            ),
          ),
          Text('Bhoomi: ${state.toUpperCase()}'),
        ],
      ),
    );
  }
}
