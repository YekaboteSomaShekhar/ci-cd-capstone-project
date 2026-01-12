#!/bin/bash
curl http://localhost:5000/health || exit 1
echo "Deployment successful"
