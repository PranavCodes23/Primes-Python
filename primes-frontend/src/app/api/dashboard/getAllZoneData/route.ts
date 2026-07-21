import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/v1/dashboard/zone-data', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      cache: 'no-store'
    });

    if (!response.ok) {
      throw new Error(`Failed to fetch from FastAPI backend: ${response.status}`);
    }

    const data = await response.json();
    return NextResponse.json(data);
  } catch (error) {
    console.error('API proxy error:', error);
    return NextResponse.json(
      { error: 'Failed to fetch data from Python API' }, 
      { status: 500 }
    );
  }
}
